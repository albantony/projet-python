#Test de la fonction d'affichage graphique
import sys
sys.path.append("swap_puzzle/")

from grid import Grid 
import pygame as pg

g = Grid.grid_from_file("input/grid1.in")
pg.init()
SURF=pg.display.set_mode((1450,1000))
while(True):
    g.graphic(SURF)
    for event in pg.event.get():
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                sys.exit()