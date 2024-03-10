#Testing file for BFS methods
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph
from grid import Grid
from grid import string_to_grid
from bfs_solver import bfs,bfs_evo

class Test_Swap(unittest.TestCase):
        

    def test_graph(self):
        #Test to verify that bfs works with a given graph
        g = Graph.graph_from_file("input/graph1.in")
        reponses=[(9,16,2,[9, 4, 16]),(13,14,2,[13, 2, 14]),(16,18,2,[16, 15, 18])]
        for src,dst,n,l in reponses:
            self.assertEqual(g.bfs(src,dst),l)
            
    def test_bfs(self):
        #Test to verify that grid to graph conversion works and applying bfs on it also works
        #It can't be tested for large dimensions as creating the entire graph of grids is space expensive
        print("BFS test")
        print(" ")
        m1=[[1,2],[4,3]]
        print(m1)
        print("BFS path for this matrix:")
        print(bfs(Grid(2,2,m1)))
        print(" ")
        m2=[[2,4],[1,5],[3,6]]
        print(m2)
        print("BFS path for this matrix:")
        print(bfs(Grid(3,2,m2)))
        #Can't do high dimensionnal tests, bfs is too expensive
        




    def test_bfs_evo(self):
        print("BFS evo test")
        print(" ")
        m1=[[1,2],[4,3]]
        print(m1)
        print("BFS evo path for this matrix:")
        print(bfs(Grid(2,2,m1)))
        print(" ")
        m2=[[2,4],[1,5],[3,6]]
        print(m2)
        print("BFS evo path for this matrix:")
        print(bfs(Grid(3,2,m2)))


if __name__ == '__main__':
    unittest.main()