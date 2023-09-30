import math


def heuristics(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return abs(x2 - x1) + abs(y2 - y1)


def hypotenuseHeuristics(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return math.sqrt(abs(x2 - x1)**2 - abs(y2 - y1)**2)
