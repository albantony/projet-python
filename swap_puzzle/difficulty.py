from grid import Grid
import math
import random
from A_star import A_star


#Dictionnary values can be modified and heavily depend on grid dimensions to find adequate grids
dico = {'facile': [0, 10], 'moyen': [10, 20], 'difficile': [20, math.inf]}
#To avoid infinite loops
lim=25


def difficulty(difficulte, n, m):
    #Randomly generating grids and calulating A* path length on these grids until finding desired path legth
    a, b = dico[difficulte]
    count = -1
    cpt=0
    while count < a or count > b:
        if cpt>lim:
            return "Not found"
        L = list(range(1, n * m + 1))
        mat = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                k = random.randint(0, len(L) - 1)
                mat[i][j] = L.pop(k)
        #BFS gives minimal length but A* is faster so we choose it to find grids in high dimensions
        count = len(A_star(Grid(m, n, mat)))
        cpt+=1
    return mat

#We get not found because it's impossible to find a 20+ path length for a 2 dimensionnal array
print(difficulty('difficile',2,2))

print(difficulty('facile', 2, 2))
print(difficulty('moyen', 3, 3))
print(difficulty('difficile', 4, 4))
