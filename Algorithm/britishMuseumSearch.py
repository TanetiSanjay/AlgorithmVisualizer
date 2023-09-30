from queue import Queue
import pygame
from util.reconstruct_path import reconstructPath


def britishMuseumSearchAlgorithm(funcDraw, Grid, Start, End):
    openSet = Queue()
    openSet.put(Start)

    cameFrom = {}

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        current = openSet.get()

        if current == End:
            reconstructPath(Start, cameFrom, End, funcDraw)
            Start.makeStart()
            End.makeEnd()
            return True

        for neighbor in current.neighbors:
            if neighbor not in cameFrom:
                cameFrom[neighbor] = current
                openSet.put(neighbor)
                neighbor.makeOpen()

        funcDraw()

        if current != Start:
            current.makeClosed()

    return False
