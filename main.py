import pygame
import util.grids
import util.draw
import util.positions

from Algorithm.britishMuseumSearch import britishMuseumSearchAlgorithm
from Algorithm.DepthFirstSearch import dfsAlgorithm
from Algorithm.BreadthFirstSearch import bfsAlgorithm
from Algorithm.HillClimbingSearch import hillClimbingSearch
from Algorithm.BeamSearch import beamSearch
from Algorithm.Oracle import oracleSearch
from Algorithm.branchAndBound import branchAndBound
from Algorithm.branchAndBoundPlusEstimatedHeuristics import branchAndBoundPlusEstimatedHeuristics
from Algorithm.branchAndBoundPlusExtensionList import branchAndBoundPlusExtensionList
from Algorithm.A_Star import aStar

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Taneti Sanjay Algorithm Visualizer")


a = '''
Please choose an options:
1.  British Museum Search
2.  Depth First Search
3.  Breadth First Search
4.  Hill Climbing Search
5.  Beam Search
6.  Oracle Search
7.  Branch and Bound
8.  Branch and Bound + Estimated Heuristics
9.  Branch and Bound + Extension List 
10. A Star
Please enter your choice: 
'''


def main(win, width):
    pygame.init()

    ROWS = 50
    grid = util.grids.makeGrid(ROWS, width)

    start = None
    end = None
    run = True
    choice = int(input(a))

    while run:
        util.draw.draw(win, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = util.positions.getClickedPosition(position, ROWS, width)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.makeStart()

                elif not end and node != start:
                    end = node
                    end.makeEnd()

                elif node != end and node != start:
                    node.makeBarrier()

            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, col = util.positions.getClickedPosition(position, ROWS, width)
                node = grid[row][col]
                node.reset()

                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.updateNeighbors(grid)

                    if choice == 1:
                        if britishMuseumSearchAlgorithm(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    elif choice == 2:
                        if dfsAlgorithm(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    elif choice == 3:
                        if bfsAlgorithm(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    elif choice == 4:
                        if hillClimbingSearch(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    elif choice == 5:
                        n = int(input("Please enter beam width: "))
                        if beamSearch(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end, n):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    elif choice == 6:
                        if oracleSearch(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    elif choice == 7:
                        if branchAndBound(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    elif choice == 8:
                        if branchAndBoundPlusEstimatedHeuristics(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    elif choice == 9:
                        if branchAndBoundPlusExtensionList(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    elif choice == 10:
                        if aStar(lambda: util.draw.draw(win, grid, ROWS, width), grid, start, end):
                            print("Path Found")

                        else:
                            print("Path Not Found")

                    if event.key == pygame.K_c:
                        start = None
                        end = None
                        grid = util.grids.makeGrid(ROWS, width)

    pygame.quit()


if __name__ == '__main__':
    main(WIN, WIDTH)
