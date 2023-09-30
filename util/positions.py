
def getClickedPosition(position, rows, width):
    gap = width//rows
    y, x = position
    row = y//gap
    col = x//gap

    return row, col
