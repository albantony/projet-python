#Test file for A* methods
import sys 
sys.path.append("swap_puzzle/")
import random
from A_star import *


print("A_star test")
m1=[[4, 3], [2, 1]]
print(m1)
print("A_star path for this matrix:")
print(A_star(Grid(2, 2, m1))) 
print(" ")
m2=[[3,4],[2,5],[1,6]]
print(m2)
print("A_star path for this matrix:")
print(A_star(Grid(3,2,m2)))
print(" ")
L=list(range(1,17))
m3=[[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        k=random.randint(0,len(L)-1)
        m3[i][j]=L.pop(k)
#Testing for a random matrix it may take a while (uncomment the following line)
print(A_star(Grid(4,4,m3)))



#Uncomment for A_star vizualisation
#A_star_vizu(Grid(2,2,m1))
#A_star_vizu(Grid(3,2,m2))
#A_star_vizu(m3)
