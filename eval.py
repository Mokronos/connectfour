import numpy as np
from mcts import get_best_valued_child
np.set_printoptions(threshold=np.nan)


x=np.loadtxt("test.txt")
ini=np.array([[1,0,2,],[1,0,2],[0,0,0]])


print(x)
get_best_valued_child(x,ini,1)

