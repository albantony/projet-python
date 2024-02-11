from grid import Grid
import numpy as np

class Solver(): 
    def __init__(self,initial_state):
        self.initial_state=initial_state
    
    def get_solution(self):
        n,m=len(self.initial_state),len(self.initial_state[0])
        tab_dist={self.initial_state:0}
        prev={}
        final_state=[list(range(k,k+m)) for k in range (1,n,m)]
        def find_num(x,mat):
            for i in range(n):
                for j in range(m):
                    if mat[i][j]==x:
                        return i,j
        def coord_num(x):
            for i in range(n):
                for j in range(m):
                    if i*m+j+1==x:
                        return i,j
        def dist(x,y):
            x1,y1=x
            x2,y2=y
            return np.sqrt((x1-x2)**2+(y1-y2)**2)
        def sort_fun(mat):
            def h(mat):
                sum=0
                for x in range(1,n*m):
                    sum+=dist(coord_num(x,mat),find_num(x,mat))
                return sum
            return tab_dist[mat]+h(mat)
        def swap(mat,x,y):
            a,b=x
            c,d=y
            mat[a][b],mat[c][d]=mat[c][d],mat[a][b]
        traites=[]
        atraiter=[self.initial_state]
        run=True
        while(run):
            atraiter.sort(key=sort_fun)
            current=atraiter.pop(0)
            for i in range(n):
                for j in range(m):
                    for r1,r2 in [(1,0),(0,1),(-1,0),(0,-1)]:
                        if i+r1 in list(range(n)) and j+r2 in list(range(m)):
                            new_mat=current.copy()
                            swap(new_mat,(i,j),(i+r1,i+r2))
                            if all((new_mat[i][j]==final_state[i][j] for i in range(n)) for j in range(m)):
                                run=False
                            elif not(new_mat in traites):
                                atraiter.append(new_mat)
                            if new_mat not in tab_dist.keys():
                                tab_dist[new_mat]=tab_dist[current]+1
                                prev[new_mat]=current
                            traites.append(new_mat)
            res=[]
            current_mat=final_state
            while(not(all((current_mat[i][j]==self.initial_state[i][j] for i in range(n)) for j in range(m)))):
                current_mat=prev[current_mat]
            


                            



    

        

