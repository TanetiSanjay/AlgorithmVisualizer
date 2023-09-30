import pygame
from queue import PriorityQueue
from util.heuristics import heuristics
from util.reconstruct_path import reconstructPath


def beamSearch(funcDraw, Grid, Start, End, beam_width):
    openSets = [PriorityQueue() for _ in range(beam_width)]
    openSetHash = [set() for _ in range(beam_width)]
    cameFrom = [{} for _ in range(beam_width)]
    gScore = [{node: float("inf") for row in Grid for node in row} for _ in range(beam_width)]
    fScore = [{node: float("inf") for row in Grid for node in row} for _ in range(beam_width)]

    for i in range(beam_width):
        openSets[i].put((0, i, Start))
        gScore[i][Start] = 0
        fScore[i][Start] = heuristics(Start.getPosition(), End.getPosition())
        openSetHash[i].add(Start)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        # Explore the beams
        for i in range(beam_width):
            if not openSets[i].empty():
                current = openSets[i].get()[2]
                openSetHash[i].remove(current)

                if current == End:
                    reconstructPath(Start, cameFrom[i], End, funcDraw)
                    End.makeEnd()
                    return True

                for neighbor in current.neighbors:
                    temp_G_score = gScore[i][current] + 1

                    if temp_G_score < gScore[i][neighbor]:
                        cameFrom[i][neighbor] = current
                        gScore[i][neighbor] = temp_G_score
                        fScore[i][neighbor] = temp_G_score + heuristics(neighbor.getPosition(), End.getPosition())

                        if neighbor not in openSetHash[i]:
                            openSets[i].put((fScore[i][neighbor], i, neighbor))
                            openSetHash[i].add(neighbor)
                            neighbor.makeOpen()

                funcDraw()

                if current != Start:
                    current.makeClosed()

    return False
