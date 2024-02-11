from grid import Grid


def naive_solver(grid):
    """This function takes any grid in parameter and returns the sorted grid with the list of swaps 
    used to get to the sorted grid"""
    """How this function works is that, in ascending order (Necessary condition), numbers are put in the right spot"""
    move_list=[]
    for i in range(1,grid.m*grid.n+1):
        for k in range(grid.m):
            for l in range(grid.n):
                if grid.state[k][l]==i:
                    x,y=(i-1)//grid.m,(i-1)%grid.m
                    #To find out if i is located right or left of its wanted position 
                    if l<y:
                        r=1
                    elif l>y:
                        r=-1
                    list=[]
                    while(l!=y):
                        list.append(((k,l),(k,l+r)))
                        move_list.append(((k,l),(k,l+r)))
                        l+=r
                    while(k>x):
                        list.append(((k,l),(k-1,l)))
                        move_list.append(((k-1,l),(k,l)))
                        k-=1
                    grid.swap_seq(list)
    return grid,move_list

g,m=naive_solver(Grid(2,2,[[3,4],[2,1]]))
print(g,m)
       

                        
                    
