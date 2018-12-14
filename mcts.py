from pathlib import Path
import numpy as np
from random import *
from ttt import update
import time
np.set_printoptions(threshold=np.nan,precision=2,suppress=True)
dimensionx=3
dimensiony=3
backtrack=[[]]
extra_data_per_state=2
ini=np.zeros((3,3))
data=np.zeros((1,ini.flatten().size+extra_data_per_state))
f=0 #reset after every iteration .. to signal that this is first state
action_space=9
x=np.zeros((1,dimensiony*dimensionx+extra_data_per_state))


#w,l,board=update(board,0,1)

#print(board)
#print(x)

#print(board1)
#print(board2)


#print(z)



# add flattened state array + visit_count + value to data/memory
def addState(data,state):
    if data_state(data,state)==0:        
        state=s1D(state)
        state=np.append(state,[[0,0]])
        state=np.reshape(state,(1,state.size))
        data=np.concatenate((data,state))
        return data
    return data

# add flattened state to backtrack data
def addBacktrack(data,state):
    if data_state(data,state)==0:
        state=s1D(state)
        state=np.reshape(state,(1,state.size))
        data=np.concatenate((data,state))
        return data
    return data

#returns visitcount for given state
def visitcount(data,state):
    state=s1D(state)
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if(np.array_equal(datax[i],state)):
            return data[i,data.shape[1]-2]
    return 0

#returns value for given state
def value(data,state):
    state=s1D(state)
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if(np.array_equal(datax[i],state)):
            return data[i,data.shape[1]-1]
    return 0

#increases visitcount by 1 for given state in given data
def up_visitcount(data,state):
    state=s1D(state)
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if(np.array_equal(datax[i],state)):
            data[i,data.shape[1]-2]+=1
    
    return data
#increases value by given value for given state in given data
def up_value(data,state,value):
    state=s1D(state)
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if(np.array_equal(datax[i],state)):
            data[i,data.shape[1]-1]=data[i,data.shape[1]-1]+value

    return data
#returns 2*actions array with visits,values for each action(action following child)
def collect_possible_childs(state,player,data):
    
    state=s2D(state)
    x=get_actions(state,player)
    childs=np.zeros((x.size,state.size+2))
    
    for i in range(x.size):
        next_state=update(state,x[i],player)[2]
        if not (np.array_equal(next_state,state)):
            childs[i,0:state.size]=next_state.flatten()
            childs[i,childs.shape[1]-2]=visitcount(data,next_state)
            childs[i,childs.shape[1]-1]=value(data,next_state)
    return childs
# return 1 if state is in data, 0 if state is not in data
def data_state(data,state):
    for i in range(data.shape[0]):
        if np.array_equal(data[i,0:state.size],state):
            return 1

    return 0



#plays out a game from given state with given player at random
def playout(state,player):
    #w=3 ... 3 for game not finished/sync with update function
    w=3
    state=s2D(state)
    p=player
    while w==3:
        c=randint(0,action_space-1)
        w,l,state=update(state,c,p)
        if l==1:
            p=(p%2)+1
    
    #playout went from the child of the leaf and started with opposite player to the player of the leaf ... if winning player is player of leaf, the reward should be positive .. we change player twice (1. in call of function, 2. after w changed in while it gets changed 1 last time) so if the winning player == p .. pos reward

   # if player==p:
   #     return w
   #     
   # return -w
    return w





def check_if_leaf(state,player):

    childs=collect_possible_childs(state,player,data)
    unvisited=np.empty(0)
    
    for i in range(childs.shape[0]):
        if childs[i,childs.shape[1]-2]==0:
            unvisited=np.append(unvisited,i)
    
    return unvisited

def backprop(backtrack,data,value):

    for i in range(backtrack.shape[0]):
        data=up_visitcount(data,backtrack[i])
        
        for j in range(data.shape[0]):
            if all(backtrack[i,0:backtrack.shape[1]] == data[j,0:data.shape[1]-2]):
               data=up_value(data,backtrack[i],value)
    
    return data

#transform state to 2D array
def s2D(state):

    if len(state.shape)==2:
        return state
    elif len(state.shape)==1:
        state=np.reshape(state,(-1,dimensionx))
        return state

#transform state to 1D array
def s1D(state):

    if len(state.shape)==1:
        return state
    elif len(state.shape)==2:
        state=state.flatten()
        return state

def get_actions(state,player):
    actions=[]
    state=s2D(state).copy()
    for i in range(action_space):
        if update(state,i,player)[1]==1:
            actions.append(i)

    return np.array(actions)


def change_value_sign(data):
    for i in range(data.shape[0]):
        data[i,data.shape[1]-1]=-data[i,data.shape[1]-1]
    return data

def get_best_child(childs):
    utc=np.zeros(childs.shape[0])
    #parent visitcount = sum of child visitcounts
    pv=0
    for i in range(childs.shape[0]):
        pv+=childs[i,childs.shape[1]-2]
    for i in range(childs.shape[0]):
        utc[i]=(childs[i,childs.shape[1]-1]/childs[i,childs.shape[1]-2])+(2**0.5)*((np.log(pv)/childs[i,childs.shape[1]-2])**0.5)
    max_utc=np.argmax(utc)
    #print("max_utc:")
    #print(max_utc)
    return childs[max_utc,0:childs.shape[1]-2]

def get_best_valued_child(data,state,player):
    c=collect_possible_childs(state,player,data)
    values=np.zeros((c.shape[0]))
    for i in range(c.shape[0]):
        values[i]=c[i,c.shape[1]-1]
    bv=np.argmax(values)
    return c[bv]

def filename():
    c=0
    n=Path("test.txt")
    while n.is_file():
        c+=1
        n=Path("test(%d).txt" % c)
        
    return n


def mcts(data,state,player,backtrack):
    
    #selection: select best states according to policy(rewards/visits) until state has 1 or more unvisited children
    #expand: select 1 random unvisited child and add it to tree with 0 value, 0 visits
    #simulation: simulate from created unvisited child to end with random actions and get reward
    #backpropagation: update stats of all nodes traveled down to simulation ... all visits +1 / pos. reward for all  nodes opposite of winner, neg. reward for all nodes of winner (pos reward for the states that are used to determine the best action for the winner ... which are the states in which the loser needs choose an action)
    #track states while selecting and expanding to update easy while backpropagating
    #print("state:")
    #print(state)
    #plan:
    #inputstate player1s turn:
    #---select state but reverse sign of data when action for player 2 needs to be selected to select highest value(is lowest value in main data)

    
    


    global f
    
    #check if this is the first recursive/if there is a backtrack
    #first recursive: make the current state the backtrack array and reshape it to accept more states
    if f==0:
        backtrack=s1D(state).copy()
        backtrack=np.reshape(backtrack,(-1,backtrack.shape[0]))
        f=1
    #not first recursive: add current state to backtrack array
    else:
        backtrack=addBacktrack(backtrack,state)
    #change value sign ... 2nd player wants to select the best states, which are the best for player 1 
    #print("backtrack:")
    #print(backtrack)
    if player==2:
        data=change_value_sign(data)
    
    childs=collect_possible_childs(state,player,data)
    
    if player==2:
        data=change_value_sign(data)
    
    #print("childs:")
    #print(childs)
    unvisited=check_if_leaf(state,player)
    #print("unvisited:")
    #print(unvisited)
    #reverse sign only when selecting ... dont reverse it for backprop it only matters what player won not what player started the backtrack
    #if current state is terminal state, no expansion/simulation needed, get value of terminal state and backprop

    if get_actions(state,player).size==0:
        state=s2D(state)
        cpv=update(state,None,player)[0]

        data=backprop(backtrack,data,cpv)
        return data


    if unvisited.size==0:

        # select next child and remember it for backpropagation
        next_state=get_best_child(childs)
        #print("next_state")
        #print(next_state)
        data=mcts(data,next_state,(player%2)+1,backtrack)
        return data
    else:
         
        sel_child=childs[int(unvisited[randint(0,unvisited.size-1)]),0:childs.shape[1]-2]
        sel_child=np.reshape(sel_child,(-1,dimensionx))
        #print("sel_child:")
        #print(sel_child)
        data=addState(data,sel_child)
        backtrack=addBacktrack(backtrack,sel_child)
        #print("new backtrack:")
        #print(backtrack)
        #cpv=current playout value
        cpv=playout(sel_child,(player%2)+1)
        
        #print("cpv:")
        #print(cpv)
        #print("old data:")
        #print(data)
        data=backprop(backtrack,data,cpv)
        #print("new data after backprop:")
        #print(data)
    #change value sign back so that the standard is player 1

        
    return data

#u=np.array([[1,2],[0,0]])
    
if __name__=="__main__":
    #n=filename()
    data=np.loadtxt("test(10).txt")
    oldt=0
    print(data)
    for i in range(10000):
        oldt=time.time()
        print("iteration:")
        print(i)
        f=0
        data=mcts(data,ini,1,backtrack)
        #print("data:")
        #print(data)
        if i%100==0:

            np.savetxt("test(10).txt",data)
        #print("data_shape[0]:")
        #print(data.shape[0])
        print("est. time for next 100 iterations:")
        print((time.time()-oldt)*100)
    print(data)

#    print(change_value_sign(data))

#print(data)
#np.set_printoptions(precision=0)
#x=np.array([[1.40000000,1,1],[200.999999999999999999,2,0],[0,0,0]])
#print(x)
#y=get_actions(x,2)
#print(y)
#z=update(x,0,1)[0]
#print(z)

#np.savetxt("test.txt",data)
#d=np.loadtxt("test.txt")
#print(d)
