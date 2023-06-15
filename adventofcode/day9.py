import utils

dataList = utils.readData(2022, 9, "\n")

dataExample = ['R 4','U 4','L 3', 'D 1', 'R 4', 'D 1', 'L 5','R 2']
secondDataExample = ['R 5','U 8','L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']

def headMoves(direction, headCurrentPosition):
    '''moves always just 1 step'''
    x, y = headCurrentPosition
    if direction == 'L':
        x = x - 1
    elif direction == 'R':
        x = x + 1
    elif direction == 'U':
        y = y + 1
    else:
        y = y - 1
    return (x, y)

def isTailAdjacent(headCurrentPosition, tailsCurrentPosition):
    xH, yH = headCurrentPosition
    xT, yT = tailsCurrentPosition
    
    if abs(xT - xH) > 1 or abs(yH -yT) > 1:
        return False
    return True

def tailMoves(direction, headCurrentPosition, tailsCurrentPosition):
    '''catches up with head if necessary'''
    xH, yH = headCurrentPosition
    xT, yT = tailsCurrentPosition
    if direction == 'L':
        #tail ends up right to head
        xT = xH + 1
        yT = yH
    elif direction == 'R':
        #tail ends up left to head
        xT = xH - 1
        yT = yH
    elif direction == 'U':
        #tail ends up bellow head
        xT = xH 
        yT = yH - 1
    else:
        # down
        #tail ends up above head
        xT = xH 
        yT = yH + 1
        
    return (xT, yT)

def calculatePositionsVisited(dataList):
    positionsVisitedByTail = {(0,0)}
    headCurrentPosition = (0,0)
    tailsCurrentPosition = (0,0)
    for data in dataList:
        direction, steps = data.split(' ')
        for _ in range(int(steps)):
            headCurrentPosition = headMoves(direction, headCurrentPosition)
            if not isTailAdjacent(headCurrentPosition, tailsCurrentPosition):
                tailsCurrentPosition = tailMoves(direction, headCurrentPosition, tailsCurrentPosition)
            positionsVisitedByTail.add(tailsCurrentPosition)
    return len(positionsVisitedByTail) 

def tailMovesAlternative(headCurrentPosition, tailsCurrentPosition):
    '''catches up with head if necessary
    alternative solution'''

    xH, yH = headCurrentPosition
    xT, yT = tailsCurrentPosition
    
    # Move on the x-axis:
    if xH > xT:
        xT += 1

    if xH < xT:
        xT -= 1

    if yH > yT:
        yT +=1

    if yH < yT:
        yT -=1
        
    return (xT, yT)

def calculatePositionsVisitedTail9(dataList):
    positionsVisitedByTail9 = {(0,0)}
    headCurrentPosition = (0,0)
    tailCurrentPositions = [(0,0) for _ in range(9)]
    # print(tailCurrentPositions)
    for data in dataList:
        direction, steps = data.split(' ')
        # One move
        for _ in range(int(steps)):
            headCurrentPosition = headMoves(direction, headCurrentPosition)
            changingHead = headCurrentPosition
            for index, tailCurrentPosition in enumerate(tailCurrentPositions):
                # print(index,"tail:", tailCurrentPosition,"changing head:", changingHead)
                if not isTailAdjacent(changingHead, tailCurrentPosition):
                    tailCurrentPositions[index] = tailMovesAlternative(changingHead, tailCurrentPosition)
                changingHead = tailCurrentPositions[index] 
                positionsVisitedByTail9.add(tailCurrentPositions[8])
    
    return len(positionsVisitedByTail9) 


# print(calculatePositionsVisited(dataList))

# print("tail9", calculatePositionsVisitedTail9(dataList))