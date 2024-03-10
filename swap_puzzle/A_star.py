from graph import Graph
from grid import Grid, string_to_grid
import copy
import heapq
import pygame as pg


def find_x(matrice, x, m, n):
    for i in range(m):
        for j in range(n):
            if matrice[i][j] == x:
                return i, j

def manhatan(s, m, n):
    grille = string_to_grid(s, m, n)
    distance = 0
    for i in range(1, n * m + 1):
        x, y = (i - 1) // m, (i - 1) % m
        a, b = find_x(grille, i, m, n)
        distance += abs(x - a) + abs(y - b)
    return distance

def A_star(grid):  
    #Time complexity:O(V+E)
    #This is worst case, but with a good heuristic, it's much better
    #Heapq is used to find min effectively
    graph = Graph([grid.grid_to_string])
    tab_dst={grid.grid_to_string():0}
    def h(s):
        return tab_dst[s]+manhatan(s, grid.m, grid.n)
    treating = [(h(grid.grid_to_string()),grid.grid_to_string())]
    heapq.heapify(treating)
    treated = []
    dst = Grid(grid.m, grid.n, list(list(range(i, i + grid.n)) for i in range(1, grid.n * grid.m + 1, grid.n)))
    prev = {}
    while treating != []:
        x,current = heapq.heappop(treating)
        if current == dst.grid_to_string():
            break
        current_matrix = Grid(grid.m, grid.n, string_to_grid(current, grid.m, grid.n))
        for i in range(grid.m):
            for j in range(grid.n):
                for (r1, r2) in [(1, 0), (0, 1)]:
                    x, y = i + r1, j + r2
                    if x in range(grid.m) and y in range(grid.n):
                        new_matrix = copy.deepcopy(current_matrix)
                        new_matrix.swap((x, y), (i, j))
                        new = new_matrix.grid_to_string()
                        if (current, new) not in graph.edges and (new, current) not in graph.edges:
                            graph.add_edge(current, new)
                        if new not in treated and (new not in treating[i] for i in range(len(treating))):
                            prev[new] = current
                            tab_dst[new]=tab_dst[current]+1
                            heapq.heappush(treating,(h(new),new))
        treated.append(current)
    current = dst.grid_to_string()
    res = [current]
    while current != grid.grid_to_string():
        res.append(prev[current])
        current = prev[current]
    res = list(reversed(res))
    def grid_edge_to_swap(g1, g2, m, n):
        for i in range(m):
            for j in range(n):
                if g1[i][j] != g2[i][j]:
                    for r1, r2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        x, y = i + r1, j + r2
                        if (x in range(m)) and (y in range(n)):
                            if g1[x][y] != g2[x][y]:
                                return (i, j), (x, y)
    for i in range(len(res) - 1):
        res[i] = grid_edge_to_swap(string_to_grid(res[i], grid.m, grid.n), string_to_grid(res[i + 1], grid.m, grid.n), grid.m, grid.n)
    res = res[:len(res) - 1]
    return res

#print(A_star(Grid(2, 2, [[4, 3], [2, 1]]))) 
#print("OK")

def A_star_vizu(grid):
    #Vizualition of A star swaps
    pg.init()
    path=A_star(grid)
    width,height=1450,1000
    SURF=pg.display.set_mode((width,height))
    grid.graphic(SURF)
    for cell1,cell2 in path:
        grid.swap(cell1,cell2)
        grid.graphic(SURF)
        pg.time.wait(1000)
    pg.time.wait(1000)

#A_star_vizu(Grid(3, 3, [[4, 3, 7], [2, 1,5],[8,9,6]]))