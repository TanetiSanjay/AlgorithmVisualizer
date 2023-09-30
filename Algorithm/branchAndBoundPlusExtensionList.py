import pygame
from queue import PriorityQueue
from util.reconstruct_path import reconstructPath


def branchAndBoundPlusExtensionList(funcDraw, Grid, Start, End):
    openSet = PriorityQueue()
    openSetHash = set()
    closedSet = set()  # This is the extended list
    cameFrom = {}
    gScore = {node: float("inf") for row in Grid for node in row}
    gScore[Start] = 0

    # Initialize with the Start node and its cost as the priority
    openSet.put((0, Start))
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
            Start.makeStart()
            End.makeEnd()
            return True  # Returns the optimal path

        for neighbor in current.neighbors:
            if neighbor in closedSet:  # Skip neighbors that are already in the extended list
                continue

            temp_G_score = gScore[current] + 1  # Assume cost is 1 for each edge for now

            if temp_G_score < gScore[neighbor]:  # If a shorter path to neighbor is found
                cameFrom[neighbor] = current
                gScore[neighbor] = temp_G_score

                # Use cost-so-far (gScore) as the priority
                priority = gScore[neighbor]
                openSet.put((priority, neighbor))
                openSetHash.add(neighbor)
                neighbor.makeOpen()

        funcDraw()

        if current != Start:
            current.makeClosed()

        closedSet.add(current)  # Add the current node to the extended list

    return False  # No path found
