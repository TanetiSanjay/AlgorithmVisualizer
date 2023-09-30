import Textures.colours
import pygame


class Node:

    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = Textures.colours.white
        self.neighbors = []
        self.width = width
        self.totalRows = totalRows
        self.isStartNode = False
        self.isEndNode = False
        self.isPathNode = False

    def getPosition(self):
        return self.x, self.y

    def isClosed(self):
        return self.color == Textures.colours.red

    def isOpen(self):
        return self.color == Textures.colours.green

    def isBarrier(self):
        return self.color == Textures.colours.black

    def isStart(self):
        return self.color == Textures.colours.orange

    def isEnd(self):
        return self.color == Textures.colours.turquoise

    def makeStart(self):
        if not self.isPathNode:
            self.color = Textures.colours.orange
        self.isStartNode = True

    def makeOpen(self):
        self.color = Textures.colours.green

    def makeBarrier(self):
        self.color = Textures.colours.black

    def makeEnd(self):
        if not self.isPathNode:
            self.color = Textures.colours.turquoise
        self.isEndNode = True

    def makePath(self):
        self.color = Textures.colours.purple
        self.isPathNode = True

    def makeClosed(self):
        self.color = Textures.colours.red

    def reset(self):
        self.color = Textures.colours.white

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def updateNeighbors(self, grid):
        self.neighbors = []
        if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isBarrier():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].isBarrier():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isBarrier():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].isBarrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

