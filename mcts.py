import numpy as np
from connectfour import update
dimensionx=7
dimensiony=6
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
def visitcount(data,state):
    state=state.flatten()
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            return data[i,data.shape[1]-2]
    return 0


def value(data,state):
    state=state.flatten()
    datax=np.delete(data,[[data.shape[1]-1,data.shape[1]-2]],axis=1)
    for i in range(datax.shape[0]):
        if((datax[i]==state).all()):
            return data[i,data.shape[1]-1]
    return 0




#def mcts(state):
#   w,l, update
#    return


initial_game_state=np.zeros((6,7))



data=np.zeros((1,initial_game_state.flatten().size+extra_data_per_state))
print(data)
w,l,state1=update(initial_game_state,0,1)
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
print(state2)
print("visits")
print(visitcount(data3,state1x))
print(visitcount(data3,state2))

print("break")
g=np.delete(data2,[[42,43]],axis=1)
print(g)
print(data2.shape[0])
print(data2[2,36])
