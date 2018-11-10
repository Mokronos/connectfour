import pygame 
import numpy as np

x=np.zeros((6,7))
print(x)


print("hello")


def update(board,action,player):
    if not 0<=(action)<=6:
        print("action not in action space")
        return 0
    if not 1<=player<=2:
        print("not a viable player")
        return 0
    if not board.shape==(6,7):
        print("wrong board dimensions")
        return 0




