import numpy as np
from random import *
from connectfour import update
dimensionx=7
dimensiony=6
action_space=7
extra_data_per_state=2
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
    state=state.flatten()
    state=np.append(state,[[0,0]])
    state=np.reshape(state,(1,state.size))
    data=np.concatenate((data,state))
    return data

#returns visitcount for given state
def visitcount(data,state):
    state=state.flatten()
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            return data[i,data.shape[1]-2]
    return 0

#returns value for given state
def value(data,state):
    state=state.flatten()
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            return data[i,data.shape[1]-1]
    return 0

#increases visitcount by 1 for given state in given data
def up_visitcount(data,state):
    state=state.flatten()
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            data[i,data.shape[1]-2]+=1
    
    return
#increases value by given value for given state in given data
def up_value(data,state,value):
    state=state.flatten()
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            data[i,data.shape[1]-1]=data[i,data.shape[1]-1]+value

    return
#returns 2*actions array with visits,values for each action(action following child)
def collect_possible_childs(state,player):
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
    p=player
    while w==3:
        c=randint(0,action_space-1)
        w,l,state=update(state,c,p)
        if l==1:
            p=(p%2)+1
    
    
    if player==p:
        return -w
        
    return w

def check_if_leaf(state,player):
    childs=collect_possible_childs(state,player)
    
    unvisited=np.empty(1)
    for i in range(action_space):
        if childs[i,childs.shape1[1]-2]==0:
            np.append(unvisited,i)


def mcts(state,player):
    
    #selection: select best states according to policy(rewards/visits) until state has 1 or more unvisited children
    #expand: select 1 random unvisited child and add it to tree with 0 value, 0 visits
    #simulation: simulate from created unvisited child to end with random actions and get reward
    #backpropagation: update stats of all nodes traveled down to simulation ... all visits +1 / pos. reward for all  nodes opposite of winner, neg. reward for all nodes of winner (pos reward for the states that are used to determine the best action for the winner ... which are the states in which the loser needs choose an action)
    #track states while selecting and expanding to update easy while backpropagating

    childs=collect_possible_childs(state,player)
    
    unvisited=np.empty(1)
    for i in range(action_space):
        if childs[i,childs.shape1[1]-2]==0:
            np.append(unvisited,i)

    sel_child=childs[unvisited[randint(0,unvisited.size)],0:childs.shape[1]-2]
        
    #if all(childs[,childs.shape[1]-2])==0
    
    #crv=current rollout value ... array with rollout values for every action
    crv=playout(sel_child,player)
        
    return



ini=np.zeros((6,7))
print(playout(ini,1))

data=np.zeros((1,ini.flatten().size+extra_data_per_state))
print("childs")
u=collect_possible_childs(ini,1)
print(u)
print(update(ini,1,1)[2])
print(data)
w,l,state1=update(ini,0,1)
print("state1")
state1x=state1.copy()
print(state1)
data1=addState(data,state1)
print(data1)
print("before")
print(state1)
w,l,state2=update(state1,1,2)
print("after")
print(state1)
print("after2")
print(state1x)
data2=addState(data1,state2)
print(data2)
data3=data2
data3[2,42]=7
data3[1,42]=5
data3[1,43]=2
data3[2,43]=8

print(state2)
print("visits")
print(visitcount(data3,state1x))
print(visitcount(data3,state2))
print(value(data3,state1x))
print(value(data3,state2))
print("break")
g=np.delete(data2,[[42,43]],axis=1)
print(g)
print(data2.shape[0])
print(data2[2,36])

f=np.zeros((action_space,ini.size+2))
print(state2)

f[0,0:42]=state2.flatten()
print(f[0,0:42])

print(f)
