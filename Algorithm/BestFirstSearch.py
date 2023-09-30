import pygame
from queue import PriorityQueue
from util.heuristics import heuristics
from util.reconstruct_path import reconstructPath


def bestFirstSearch(funcDraw, Grid, Start, End):
    openSet = PriorityQueue()
    openSetHash = set()
    cameFrom = {}
    gScore = {node: float("inf") for row in Grid for node in row}
    gScore[Start] = 0

    # Use only the heuristic value as the priority for BFS
    openSet.put((heuristics(Start.getPosition(), End.getPosition()), Start))
    openSetHash.add(Start)

    while not openSet.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = openSet.get()[1]
        openSetHash.remove(current)

        if current == End:
            reconstructPath(Start, cameFrom, End, funcDraw)
            End.makeEnd()
            return True

        for neighbor in current.neighbors:
            temp_G_score = gScore[current] + 1

            if temp_G_score < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = temp_G_score

                # Use the heuristic value as the priority for BFS
                priority = heuristics(neighbor.getPosition(), End.getPosition())
                openSet.put((priority, neighbor))
                openSetHash.add(neighbor)
                neighbor.makeOpen()

        funcDraw()

        if current != Start:
            current.makeClosed()

    return False
