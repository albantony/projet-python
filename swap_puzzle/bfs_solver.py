from graph import Graph
from grid import Grid
from grid import string_to_grid
import copy
import unittest


def bfs(grid):
    #Time complexity of function:O(Card(V)+Card(E)+G) V=vertices,E=edges,G=graph construction cost so O((nm)!(1+(n*(m-1)+(n-1)*m)/2)+G)
    graph=grid.grid_to_graph()
    src,dst=grid.grid_to_string(),Grid(grid.m,grid.n,list(list(range(i,i+grid.n)) for i in range(1,grid.n*grid.m+1,grid.n))).grid_to_string()
    #Function to determine what swap is made between two different grids 
    def grid_edge_to_swap(g1,g2,m,n):
        for i in range(m):
            for j in range(n):
                if g1[i][j]!=g2[i][j]:
                    for r1,r2 in [(1,0),(0,1),(-1,0),(0,-1)]:
                        x,y=i+r1,j+r2
                        if x in list(range(m)) and y in list(range(n)):
                            if g1[x][y]!=g2[x][y]:
                                return((i,j),(x,y))
    res=graph.bfs(src,dst)
    #Converting list of states to swaps used to travel between states
    for i in range(len(res)-1):
        res[i]=grid_edge_to_swap(string_to_grid(res[i],grid.m,grid.n),string_to_grid(res[i+1],grid.m,grid.n),grid.m,grid.n)
    res=res[:len(res)-1]
    return res





def bfs_evo(grid):   
    """This function is similar to the bfs resolution in "test_bfs" but instead of creating a graph of all possible
    grids before exploring it, we define edges and vertices from the starting position, following a bfs logic, but stop
    when finding the sorted grid
    """
    #Same time complexity as bfs minus G cost
    graph=Graph([grid.grid_to_string])
    treating=[grid.grid_to_string()]
    treated=[]
    dst=Grid(grid.m,grid.n,list(list(range(i,i+grid.n)) for i in range(1,grid.n*grid.m+1,grid.n)))
    prev={}
    while(treating!=[]):
        current=treating.pop(0)
        if current==dst.grid_to_string():
            break
        current_matrix=Grid(grid.m,grid.n,string_to_grid(current,grid.m,grid.n))
        for i in range(grid.m):
            for j in range(grid.n):
                for (r1,r2) in [(1,0),(0,1)]:
                    x,y=i+r1,j+r2
                    if x in list(range(grid.m)) and y in list(range(grid.n)):
                        #Adding "adjacent" matrix to list of vertices that need to be treated
                        new_matrix=copy.deepcopy(current_matrix)
                        new_matrix.swap((x,y),(i,j))
                        new=new_matrix.grid_to_string()
                        if (current,new) not in graph.edges and (new,current) not in graph.edges:
                            graph.add_edge(current,new)
                        if new not in treated and new not in treating:
                            treating.append(new)
                            prev[new]=current
        treated.append(current)
    current=dst.grid_to_string()
    res=[current]
    while(current!= grid.grid_to_string()):
        res.append(prev[current])
        current=prev[current]
    res=list(reversed(res))
    #See explanation in bfs
    def grid_edge_to_swap(g1,g2,m,n):
            for i in range(m):
                for j in range(n):
                    if g1[i][j]!=g2[i][j]:
                        for r1,r2 in [(1,0),(0,1),(-1,0),(0,-1)]:
                            x,y=i+r1,j+r2
                            if x in list(range(m)) and y in list(range(n)):
                                if g1[x][y]!=g2[x][y]:
                                    return((i,j),(x,y))
    for i in range(len(res)-1):
        res[i]=grid_edge_to_swap(string_to_grid(res[i],grid.m,grid.n),string_to_grid(res[i+1],grid.m,grid.n),grid.m,grid.n)
    res=res[:len(res)-1]
    return res

assert(bfs_evo(Grid(2,2,[[4,3],[2,1]]))==[((0, 0), (1, 0)), ((0, 0), (0, 1)), ((1, 0), (1, 1)), ((0, 0), (1, 0))])
print("OK")