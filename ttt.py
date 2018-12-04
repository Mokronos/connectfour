import numpy as np

ini=np.zeros((3,3))
action_space=ini.size

def player_legal(board,player):
    board=s1D(board).copy()
    c1=0
    c2=0
    for i in range(board.size):
        if board[i]==1:
            c1+=1
        if board[i]==2:
            c2+=1
    p=0
    if c1==c2:
        p=1
    elif c1+1==c2:
        p=2

    if p==player:
        return 1

    return 0

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


def legal(board,action,player):
    if player_legal(board,player)==0:
        return 0
    board=s1D(board).copy()
    if board[action]==0:
        return 1
    return 0

def move(board,action,player):
    board=s1D(board).copy()
    
    board[action]=player
    return board

def update(board,action,player):
    
    board=board.copy()
    if legal(board,action,player)==0:
        return 3,0,board
    
    board=move(board,action,player)

    w1=check_if_won(board)
    w=3
    if w1==3:
        w=0
    elif player==1:
        if w1==1:
            w=1
        elif w1==2:
            w=-1
    elif player==2:
        if w1==2:
            w=1
        elif w1==1:
            w=-1

    return w,1,board

    #return win,legal,board




print(ini)
print(legal(ini,1,1))




