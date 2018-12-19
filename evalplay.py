import numpy as np
import time
from connectfour import update
from mcts import s2D
from mcts import s1D
from mcts import get_best_valued_child
from mcts import change_value_sign
from mcts import collect_possible_childs
from mcts import mcts
np.set_printoptions(threshold=np.nan,suppress=True)


def search5(data,state,player):
    backtrack=[[]] 
    oldt=time.time()
    print("searching...")
    while oldt+60>time.time():
        f=0
        data,backtrack,f=mcts(data,state,player,backtrack,f)
    return data


def play():
    board=np.zeros((6,7))
    backtrack=[[]]
    x=np.loadtxt("test(9).txt")
    w=3
    l=0
    pc=0
    player=1
    print(board)
    while(w==3):
        
        x=search5(x,board,player)
        if player==2:
            x=change_value_sign(x)
        print(s2D(get_best_valued_child(x,board,player)[0:(get_best_valued_child(x,board,player)).size-2]))        
        if player==2:
            x=change_value_sign(x)

        action=input("player "+str(player)+", choose action 0-6:")
        action=int(action)
        w,l,board=update(board,action,player)
        print("action taken: "+str(action)+" by player: "+str(player))
        if l==1:
            pc+=1
            player=(pc%2)+1
        print(board)
#print(np.zeros((6,7)))
play()
