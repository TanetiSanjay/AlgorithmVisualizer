import pygame.draw
import Textures.colours
from util.Node import Node


def makeGrid(row, width):
    grid = []
    gap = width//row

    for i in range(row):
        grid.append([])
        for j in range(row):
            node = Node(i, j, gap, row)
            grid[i].append(node)

    return grid


def drawGrid(win, rows, width):
    gap = width//rows

    for i in range(rows):
        pygame.draw.line(win, Textures.colours.grey, (0, i*gap), (width, i*gap))
        for j in range(rows):
            pygame.draw.line(win, Textures.colours.grey, (j*gap, 0), (j*gap, width))
