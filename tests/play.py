#graphics display test
import sys
sys.path.append("swap_puzzle/")

from grid import Grid 
import pygame as pg

largeur=1450
hauteur=1000


#Displaying a grid as long as escape key isn't pressed
g = Grid.grid_from_file("input/grid1.in")
pg.init()
SURF=pg.display.set_mode((largeur,hauteur))
clicked=False
coords=None
while(True):
    x0,y0,x1,y1=g.graphic(SURF,coords)
    if g.is_sorted():
        SURF.blit(pg.font.SysFont(None,30).render("Gagné!",True,(0,0,0)),(100,500))
        pg.display.update()
    for event in pg.event.get():
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                sys.exit()
        elif event.type==pg.MOUSEBUTTONDOWN:
                y,x=pg.mouse.get_pos()
                def mouse_to_mat_coords(x,y):
                    xc,yc=x0,y0
                    while (xc+(x1-x0)/(g.m-1)<x):
                        xc+=(x1-x0)/(g.m-1)
                    while (yc+(y1-y0)/(g.n-1)<y):
                        yc+=(y1-y0)/(g.n-1)
                    return round((xc-x0)*(g.m-1)/(x1-x0)),round((yc-y0)*(g.n-1)/(y1-y0))
                x,y=mouse_to_mat_coords(x,y)
                if x in list(range(g.m)) and y in list(range(g.n)):
                    if not(clicked):
                        clicked=True
                        coords=x,y
                    else:
                        a,b=coords
                        g.swap((a,b),(x,y))
                        coords=None
                        clicked=False
        


                    