
import numpy as np
from random import *
from connectfour import update
np.set_printoptions(threshold=np.nan)
dimensionx=7
dimensiony=6
backtrack=[[]]
extra_data_per_state=2
ini=np.zeros((6,7))
data=np.zeros((1,ini.flatten().size+extra_data_per_state))
f=0 #reset after every iteration .. to signal that this is first state
action_space=7
x=np.zeros((1,dimensiony*dimensionx+extra_data_per_state))
x[0,x.size-3]=7
x[0,x.size-2]=8
x[0,x.size-1]=9


board=np.zeros((6,7))

#w,l,board=update(board,0,1)

#print(board)
#print(x)
v=2
q=5

board1=board.flatten("F")
board1=np.append(board1,[[v,q]])
#print(board1)
board2=np.reshape(board1,(1,dimensiony*dimensionx+extra_data_per_state))
#print(board2)
z=np.concatenate((x,board2))


#print(z)



# add flattened state array + visit_count + value to data/memory
def addState(data,state):
    state=s1D(state)
    state=np.append(state,[[0,0]])
    state=np.reshape(state,(1,state.size))
    data=np.concatenate((data,state))
    return data

# add flattened state to backtrack data
def addBacktrack(data,state):
    state=s1D(state)
    state=np.reshape(state,(1,state.size))
    data=np.concatenate((data,state))
    return data


#returns visitcount for given state
def visitcount(data,state):
    state=s1D(state)
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            return data[i,data.shape[1]-2]
    return 0

#returns value for given state
def value(data,state):
    state=s1D(state)
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            return data[i,data.shape[1]-1]
    return 0

#increases visitcount by 1 for given state in given data
def up_visitcount(data,state):
    state=s1D(state)
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            data[i,data.shape[1]-2]+=1
    
    return data
#increases value by given value for given state in given data
def up_value(data,state,value):
    state=s1D(state)
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            data[i,data.shape[1]-1]=data[i,data.shape[1]-1]+value

    return data
#returns 2*actions array with visits,values for each action(action following child)
def collect_possible_childs(state,player,data):
    
    state=s2D(state)
    childs=np.zeros((action_space,state.size+2))
    
    for i in range(action_space):
        next_state=update(state,i,player)[2]
        childs[i,0:state.size]=next_state.flatten()
        childs[i,childs.shape[1]-2]=visitcount(data,next_state)
        childs[i,childs.shape[1]-1]=value(data,next_state)
    return childs

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

    if player==p:
        return w
        
    return -w

def check_if_leaf(state,player):

    childs=collect_possible_childs(state,player,data)
    unvisited=np.empty(0)
    for i in range(action_space):
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




def change_value_sign(data):
    for i in range(data.shape[0]):
        data[i,data.shape[1]-1]=-data[i,data.shape[1]-1]
    return data

def get_best_child(childs):
    utc=np.zeros(childs.shape[0])
    for i in range(childs.shape[0]):
        utc[i]=childs[i,childs.shape[1]-1]/childs[i,childs.shape[1]-2]
    max_utc=np.argmax(utc)
    print("max_utc:")
    print(max_utc)
    return childs[max_utc,0:childs.shape[1]-2]


def mcts(data,state,player,backtrack):
    
    #selection: select best states according to policy(rewards/visits) until state has 1 or more unvisited children
    #expand: select 1 random unvisited child and add it to tree with 0 value, 0 visits
    #simulation: simulate from created unvisited child to end with random actions and get reward
    #backpropagation: update stats of all nodes traveled down to simulation ... all visits +1 / pos. reward for all  nodes opposite of winner, neg. reward for all nodes of winner (pos reward for the states that are used to determine the best action for the winner ... which are the states in which the loser needs choose an action)
    #track states while selecting and expanding to update easy while backpropagating
    print("state:")
    print(state)
    global f

    if f==0:
        backtrack=s1D(state).copy()
        backtrack=np.reshape(backtrack,(-1,backtrack.shape[0]))
        f=1
    else:
        backtrack=addBacktrack(backtrack,state)
    #change value sign ... 2nd player wants to select the best states, which are the best for player 1 
    print("backtrack:")
    print(backtrack)
    if player==2:
        data=change_value_sign(data)
    
    childs=collect_possible_childs(state,player,data)
    print("childs:")
    print(childs)
    unvisited=check_if_leaf(state,player)
    print("unvisited:")
    print(unvisited)

    if unvisited.size==0:

        # select next child and remember it for backpropagation
        next_state=get_best_child(childs)
        if player==2:
            data=change_value_sign(data)
        data=mcts(data,next_state,(player%2)+1,backtrack)
        return data
    else:
        sel_child=childs[int(unvisited[randint(0,unvisited.size-1)]),0:childs.shape[1]-2]
        sel_child=np.reshape(sel_child,(-1,dimensionx))
        print("sel_child:")
        print(sel_child)
        data=addState(data,sel_child)
        backtrack=addBacktrack(backtrack,sel_child)
        print("new backtrack:")
        print(backtrack)
        #cpv=current playout value
        cpv=playout(sel_child,(player%2)+1)
        print("cpv:")
        print(cpv)
        print("old data:")
        print(data)
        data=backprop(backtrack,data,cpv)
        print("new data after backprop:")
        print(data)
    #change value sign back so that the standard is player 1

        if player==2:
            data=change_value_sign(data)
        return data

for i in range(9):
    print("iteration:")
    print(i)
    data=mcts(data,ini,1,backtrack)
    f=0
    print("data:")
    print(data)


np.savetxt("test.txt",data,newline="")
