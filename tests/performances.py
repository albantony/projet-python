import sys 
sys.path.append("swap_puzzle/")
from naive_solver import *
from A_star import *
from bfs_solver import *
import time 
import random
print("choisir une matrice")
x=int(input())
m1=Grid(2,2,[[3,4],[2,1]])
m2=Grid(3,3,[[3,4,7],[2,5,8],[1,6,9]])
m3=[[0]*4 for i in range(4)]
L=list(range(1,17))
for i in range(4):
    for j in range(4):
        k=random.randint(0,len(L)-1)
        m3[i][j]=L.pop(k)

if x==1:
    m=m1
elif x==2:
    m=m2
else:
    m=m3

t_naive=time.time()
for i in range(100):
    (naive_solver(m))
dtnaive=time.time()-t_naive
print(dtnaive)

t_bfs=time.time()
for i in range(1):
    (bfs(m))
dbfs=time.time()-t_bfs
print(dbfs)

t_bfs_evo=time.time()
for i in range(1):
    (bfs_evo(m))
dbfsevo=time.time()-t_bfs_evo
print(dbfsevo)


t_a_star=time.time()
for i in range(1):
    (A_star(m))
dastar=time.time()-t_a_star
print(dastar)




