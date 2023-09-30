import pygame
from util.reconstruct_path import reconstructPath


def dfsAlgorithm(funcDraw, Grid,Start, End):
    stack = [Start]
    visited = {Start}
    cameFrom = {}

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = stack.pop()

        if current == End:
            reconstructPath(Start, cameFrom, End, funcDraw)
            Start.makeStart()
            End.makeEnd()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                cameFrom[neighbor] = current
                neighbor.makeOpen()

        funcDraw()

        if current != Start:
            current.makeClosed()

    return False  # No path found
