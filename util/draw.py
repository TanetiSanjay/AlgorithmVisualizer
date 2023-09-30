import Textures.colours
import util.grids
import pygame


def draw(win, grid, rows, width):
    win.fill(Textures.colours.white)

    for row in grid:
        for node in row:
            node.draw(win)

    util.grids.drawGrid(win, rows, width)
    pygame.display.update()
