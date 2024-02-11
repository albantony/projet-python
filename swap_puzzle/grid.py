
import pygame as pg
import numpy as np
from graph import Graph
import copy
"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random

def string_to_grid(s,n,m):
    res=[([0]*n) for i in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j]=s[i*m+j]
    return res


class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def graphic(self,SURF):
        #SURF is the window that we blit things on
        #Colors that will be used to render grid
        light_gray=(210,210,210)
        black=(0,0,0)
        dark_grey=(230,230,230)
        SURF.fill(light_gray)
        font=pg.font.SysFont(None,30)
        #Coordinates should be modified according to matrix shape
        #Top left coordinates of grid matrix
        x0,y0=100,150 
        #Bot right coordinates of grid matrix
        x1,y1=500,250

        for j in range(self.n):  
            for i in range(self.m):  
                pg.draw.rect(SURF,dark_grey,[y0+(j)*(y1-y0)/(self.n-1),x0+i*(x1-x0)/(self.m-1),(y1-y0)/self.n,(x1-x0)/(self.m)])
                number=font.render(str(self.state[i][j]),True,black)
                SURF.blit(number,(y0+j*(y1-y0)/(self.n-1)+(y1-y0)/(2*self.n),x0+i*(x1-x0)/(self.m-1)+(x1-x0)/(2*self.m)))
        pg.display.update()





    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        count=1
        for i in range(self.m):
            for j in range(self.n):
                if count!=self.state[i][j]:
                    return False
        return True

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        x1,y1=cell1
        x2,y2=cell2
        if abs(x1-x2)+abs(y1-y2)>1:
            raise Exception("Impossible swap")
        self.state[x1][y1],self.state[x2][y2]=self.state[x2][y2],self.state[x1][y1]

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for c1,c2 in cell_pair_list:
            self.swap(c1,c2)
    
    def grid_to_string(self):
        s=""
        for i in range(self.m):
            for j in range(self.n):
                s+=str(self.state[i][j])
        return s


    def grid_to_graph(self):
        #Number of vertices: Cardinal of [1,nm] permutations set, so (nm)!
        #Number of edges: For every vertex (grid), you can swap positions vertically, which account for:
        #n*(m-1) swaps and horizontally, which account for (n-1)*m swaps.
        #By adding both possibilities and considering this for every vertex,
        #You have (nm)!*(n*(m-1)+(n-1)*m)/2 edges (divided by 2 because the graph is non oriented)
        graph=Graph([self.grid_to_string])
        treating=[self.grid_to_string()]
        treated=[]
        while(treating!=[]):
            current=treating.pop(0)
            current_matrix=Grid(self.m,self.n,string_to_grid(current,self.n,self.m))
            for i in range(self.m):
                for j in range(self.n):
                    for (r1,r2) in [(1,0),(0,1)]:
                        x,y=i+r1,j+r2
                        if x in list(range(self.m)) and y in list(range(self.n)):
                            new_matrix=copy.deepcopy(current_matrix)
                            new_matrix.swap((x,y),(i,j))
                            new=new_matrix.grid_to_string()
                            if (current,new) not in graph.edges and (new,current) not in graph.edges:
                                graph.add_edge(current,new)
                            if new not in treated and new not in treating:
                                treating.append(new)
            treated.append(current)
        return graph





    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


