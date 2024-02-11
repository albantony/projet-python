#Fichier pour tester la méthode BFS
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph
from grid import Grid
from grid import string_to_grid


class Test_Swap(unittest.TestCase):
        

    def test_graph(self):
        #Test to verify that bfs works with a given graph
        g = Graph.graph_from_file("input/graph1.in")
        reponses=[(9,16,2,[9, 4, 16]),(13,14,2,[13, 2, 14]),(16,18,2,[16, 15, 18])]
        for src,dst,n,l in reponses:
            self.assertEqual(g.bfs(src,dst),l)
            
    def test_bfs_1(self):
        #Test to verify that grid to graph conversion works and applying bfs on it also works
        #Time complexity of function:O(Card(V)+Card(E)) V=vertices,E=edges, so O((nm)!(1+(n*(m-1)+(n-1)*m)/2))
        g = Grid(2,2,[[4,3],[2,1]])
        graph=g.grid_to_graph()
        src,dst=g.grid_to_string(),"1234"
        #Function to determine what swap is between two different grids 
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
            res[i]=grid_edge_to_swap(string_to_grid(res[i],2,2),string_to_grid(res[i+1],2,2),2,2)
        res=res[:len(res)-1]
        self.assertEqual(res,[((0, 0), (1, 0)), ((0, 0), (0, 1)), ((1, 0), (1, 1)), ((0, 0), (1, 0))])


if __name__ == '__main__':
    unittest.main()