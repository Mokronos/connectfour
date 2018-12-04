import numpy as np

ini=np.zeros((3,3))
action_space=ini.size
dimensionx=ini.shape[1]
dimensiony=ini.shape[0]
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
    elif c2+1==c1:
        p=2
    if p==player:
        return 1

    return 0

def check_if_won(board):
    board=s2D(board).copy()
    #vertically
    for i in range(board.shape[0]):
        c1=0
        c2=0
        for j in range(board.shape[1]):
            if board[i,j]==1:
                c1+=1
                c2=0
            if board[i,j]==2:
                c1=0
                c2+=1
            if board[i,j]==0:
                c1=0
                c2=0
            if c1==3:
                print("player1 won")
                return 1
            if c2==3:
                print("player2 won")
                return 2

    #horizontally
    for j in range(board.shape[1]):
        c1=0
        c2=0
        for i in range(board.shape[0]):
            if board[i,j]==1:
                c1+=1
                c2=0
            if board[i,j]==2:
                c1=0
                c2+=1
            if board[i,j]==0:
                c1=0
                c2=0
            if c1==3:
                print("player1 won")
                return 1
            if c2==3:
                print("player2 won")
                return 2

    #diagonally_1
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            c1=0
            c2=0
            cx=j
            cy=i
            while 0<=cy<board.shape[0] and 0<=cx<board.shape[1]:
                if board[cy,cx]==1:
                    c1+=1
                    c2=0
                if board[cy,cx]==2:
                    c1=0
                    c2+=1
                if board[cy,cx]==0:
                    c1=0
                    c2=0
                if c1==3:
                    print("player1 won")
                    return 1
                if c2==3:
                    print("player2 won")
                    return 2
                cx+=1
                cy+=1

    #diagonally_2
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            c1=0
            c2=0
            cx=j
            cy=i
            while 0<=cy<board.shape[0] and 0<=cx<board.shape[1]:
                if board[cy,cx]==1:
                    c1+=1
                    c2=0
                if board[cy,cx]==2:
                    c1=0
                    c2+=1
                if board[cy,cx]==0:
                    c1=0
                    c2=0
                if c1==3:
                    print("player1 won")
                    return 1
                if c2==3:
                    print("player2 won")
                    return 2
                cx-=1
                cy+=1
    #check if board full(draw)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i,j]==0:
                return 0
    print("draw due to full board and no winner")
    return 3


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
    board=s1D(board)
    board[action]=player
    return board

def update(board,action,player):
    
    board=board.copy()
    if legal(board,action,player)==0:
        print("wrong action")
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

def play():
    board=np.zeros((3,3))
    w=3
    l=0
    pc=0 #playercounter
    player=1
    print(board)
    while(w==3):
        action=input("player "+str(player)+", choose action 0-6:")
        action=int(action)
        w,l,board=update(board,action,player)
        
        if l==1:
            print("action taken: "+str(action)+" by player: "+str(player))
            pc+=1
            player=(pc%2)+1
        
        print(s2D(board))



play()






