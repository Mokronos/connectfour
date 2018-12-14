import numpy as np
from mcts import get_best_valued_child
from mcts import change_value_sign
from mcts import s2D
np.set_printoptions(threshold=np.nan,suppress=True)

x=np.loadtxt("test(10).txt")
ini=np.array([[1,2,0],[2,1,0],[1,0,2]])
state=np.zeros((6,7))
ini4=np.array([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,1,0,2,2,2]])


player=1
print(ini)
#print(ini4)
def test(x,state,player):
    for i in range(9):
    
        state=get_best_valued_child(x,state,player)[0:9]
        print(s2D(state))
        player=(player%2)+1
        #x=change_value_sign(x)

#test(x,ini,player)
#test(x,state,player)

print(s2D(get_best_valued_child(x,ini,1)[0:(get_best_valued_child(x,ini,1)).size-2]))
