import pygame
from util.reconstruct_path import reconstructPath


def bfsAlgorithm(funcDraw, Grid, start, end):
    stack = [start]
    cameFrom = {}
    visited = set()

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        current = stack.pop()

        if current == end:
            reconstructPath(start, cameFrom, end, funcDraw)
            end.makeEnd()
            return True

        visited.add(current)

        for neighbor in current.neighbors:
            if neighbor not in visited and neighbor not in stack:
                cameFrom[neighbor] = current
                stack.append(neighbor)
                neighbor.makeOpen()

        funcDraw()

        if current != start:
            current.makeClosed()

    return False