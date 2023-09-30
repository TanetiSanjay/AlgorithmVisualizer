def reconstructPath(start, cameFrom, current, funcDraw):
    while current in cameFrom:
        current = cameFrom[current]
        current.makePath()
        funcDraw()
    start.makeStart()
