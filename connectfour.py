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
            if c1==4:
                print("player1 won")
                return 1
            if c2==4:
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
            if c1==4:
                print("player1 won")
                return 1
            if c2==4:
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
                if c1==4:
                    print("player1 won")
                    return 1
                if c2==4:
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
                if c1==4:
                    print("player1 won")
                    return 1
                if c2==4:
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

def move(board,action,player):

    for i in range(6):
        if board[i,action]!=0:
            board[i-1,action]=player
            return board
    
    board[5,action]=player
    return board



def update(board,action,player):
    boardx=board.copy()
    if legal(boardx,action,player)==0:
        print("not a legal move")
        return 0,0,boardx
    
    boardx=move(boardx,action,player)
    print(boardx) 
    w1=check_if_won(boardx)
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


    #return win,legal,board
    return w,1,boardx 
def play():
    board=np.zeros((6,7))
    w=0
    l=0
    pc=0 #playercounter
    player=1
    print(board)
    while(w==3):
        action=input("player "+str(player)+", choose action 0-6:")
        action=int(action)
        w,l,board=update(board,action,player)
        if l==1:
            pc+=1
            player=(pc%2)+1
        print("action taken: "+str(action)+" by player: "+str(player))
        print(board)

    if w==0:
        print("draw - board is full")
        
    else:
        print("player "+str(w)+" won")



#play()




#board=np.zeros((6,7))
#print(board)
#
#
#print("hello")
#
#w,l,board=update(board,6,1)
#print(board)
#
#
#w,l,board=update(board,0,2)
#print(board)
#
#w,l,board=update(board,1,1)
#print(board)
#
#w,l,board=update(board,1,2)
#print(board)
#
#w,l,board=update(board,2,1)
#print(board)
#w,l,board=update(board,2,2)
#print(board)
#w,l,board=update(board,3,1)
#print(board)
#w,l,board=update(board,2,2)
#print(board)
#w,l,board=update(board,3,1)
#print(board)
#w,l,board=update(board,3,2)
#print(board)
#w,l,board=update(board,5,1)
#print(board)
#w,l,board=update(board,3,2)
#print(board)
#w,l,board=update(board,6,1)
#print(board)

