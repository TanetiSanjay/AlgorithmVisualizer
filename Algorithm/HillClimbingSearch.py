import pygame
from util.heuristics import heuristics
from util.reconstruct_path import reconstructPath


def hillClimbingSearch(funcDraw, grid, start, end):
    open_set = [start]
    visited = set()
    found = False

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_set.pop()
        visited.add(current)

        if current == end:
            reconstructPath(start, {}, end, funcDraw)
            end.makeEnd()
            found = True
            break

        neighbors = [neighbor for neighbor in current.neighbors if neighbor not in visited]

        if not neighbors:
            # No path found, simply break out of the loop without displaying an error message
            break

        # Calculate the heuristic value for each neighbor
        neighbor_values = [(neighbor, heuristics(neighbor.getPosition(), end.getPosition())) for neighbor in neighbors]
        neighbor_values.sort(key=lambda x: x[1])  # Sort by heuristic value

        # Move to the neighbor with the lowest heuristic value (closest to the goal)
        next_node, _ = neighbor_values[0]
        next_node.makeOpen()

        # Update the current node
        current.makeClosed()

        # Update the path by marking it as purple
        current.makePath()

        open_set.append(next_node)
        funcDraw()

    return found
