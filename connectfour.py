import numpy as np

def legal(board,action,player):
        if not 0<=(action)<=6:
            print("action not in action space")
    
            return 0
        if not 1<=player<=2:
            print("not a viable player")
            return 0
        if not board.shape==(6,7):
            print("wrong board dimensions")
            return 0
        if board[0,action]!=0:
            print("wrong action_column full")
            return 0
        c1=0
        c2=0
        for i in range(6):
            for j in range(7):
                if board[i,j]==1:
                    c1 += 1
                if board[i,j]==2:
                    c2 += 1
        
        
        if (c1==c2) and (player==2):
            print("wrong player, it is player1's turn")
            return 0
        if (c1<c2):
            print("player2 went twice or too often")
            return 0
        if (c1>c2) and (player==1):
            print("wrong player, it is player2's turn")
            return 0
        print("legal move")
        return 1
def check_if_won(board):
    for i 
def update(board,action,player):

    if legal(board,action,player)==0:
        print("not a legal move")
        return 0,board

    for i in range(6):
        if board[i,action]!=0:
            board[i-1,action]=player
            return 1,board
    
    board[5,action]=player
    return 1,board

board=np.zeros((6,7))
print(board)


print("hello")

g,board=update(board,1,1)
print(board)


g,board=update(board,1,2)
print(board)


g,board=update(board,1,2)
print(board)

