import pygame
from queue import Queue


def reconstructPath(Start, cameFrom, End, funcDraw):
    path = []
    current = End

    while current != Start:
        path.append(current)
        node = cameFrom[current]
        node.makePath()  # Marks the node as part of the path
        current = node

    Start.makeStart()
    End.makeEnd()
    funcDraw()


def oracleSearch(funcDraw, Grid, Start, End):
    openQueue = Queue()
    openSet = set()
    cameFrom = {}
    gScore = {node: float("inf") for row in Grid for node in row}
    gScore[Start] = 0

    openQueue.put(Start)
    openSet.add(Start)

    while not openQueue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False  # No path found

        current = openQueue.get()
        openSet.remove(current)

        if current == End:
            reconstructPath(Start, cameFrom, End, funcDraw)
            Start.makeStart()
            End.makeEnd()
            return True  # Path found

        for neighbor in current.neighbors:
            temp_G_score = gScore[current] + 1  # Assume cost is 1 for each edge for now

            if temp_G_score < gScore[neighbor]:  # If a shorter path to neighbor is found
                cameFrom[neighbor] = current
                gScore[neighbor] = temp_G_score

                if neighbor not in openSet:
                    openQueue.put(neighbor)
                    openSet.add(neighbor)
                    neighbor.makeOpen()

        funcDraw()

        if current != Start:
            current.makeClosed()

    return False  # No path found
