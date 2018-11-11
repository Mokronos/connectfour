import pygame 
import numpy as np

x=np.zeros((6,7))
print(x)

x[1,1]=5

print(x[1,1])

print("hello")


def update(board,action,player):
    if not 0<=(action)<=6:
        print("action not in action space")
        return 0,board
    if not 1<=player<=2:
        print("not a viable player")
        return 0,board
    if not board.shape==(6,7):
        print("wrong board dimensions")
        return 0,board
    
    if board[0,action]!=0:
        print("wrong action_column full")
        return 0,board
    
    for i in range(6):
        if board[i,action]!=0:
            board[i-1,action]=player
            return 1,board




