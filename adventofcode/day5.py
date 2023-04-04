import utils
from aocd import submit

dataList = utils.readData(2022, 5,'\n')

def replaceBlankSpaces(data):
    data = data.replace("    ", " [-]").split(" ")
    return data

def createStackDict(numberOfCranes):
    stackDict = {}
    for i in range(numberOfCranes):
        stackDict[f'{i+1}'] = []
    return stackDict

def reorganizeDataByStack(cranes, stackDict, numberOfStacks):
    for k in range(len(cranes)-1, -1, -1):
        dataList = cranes[k]
        for i in range(numberOfStacks):
            if dataList[i] == '[-]':
                continue
            crane = dataList[i].replace('[',"").replace("]","")
            stackDict[f'{i+1}'].append(crane)

def organizeCraneInfo():
    cranes = []
    numberOfStacks = None
    for data in dataList:
        if '1' in data:
            numberOfStacks = len(data.split('  '))
            break
        # replace grpups of 4 spaces with " [-]"
        data = replaceBlankSpaces(data)
        cranes.append(data)
    # reorganized cranes {"1": ['M''N']}
    stackDict = createStackDict(numberOfStacks)
    reorganizeDataByStack(cranes, stackDict, numberOfStacks)
    return stackDict

def organizeMoves():
    moves = []
    for data in dataList:
        if 'move' in data:
            moves.append(data.split(" "))
    return moves

def moveCranesAround(part2=False):
    stackDict = organizeCraneInfo()
    moves = organizeMoves()
    for move in moves:
        dealWithMove(stackDict, move, part2)

    result = takeLastCranes(stackDict)
    return result

def dealWithMove(stackDict, move, part2=False):
    fromTemp = stackDict[move[3]]
    toTemp = stackDict[move[5]]
    numberOfItems = move[1]

    fromFinal, removedElements = removeElems(numberOfItems, fromTemp)
    toFinal = addElems(removedElements, toTemp, part2)

    stackDict[move[3]] = fromFinal
    stackDict[move[5]] = toFinal
    return stackDict

def removeElems(numberOfItems, affectedlist):
    fromFinal = affectedlist[0: len(affectedlist)-int(numberOfItems)]
    removedElements = affectedlist[len(affectedlist)-int(numberOfItems):]
    return fromFinal, removedElements

def addElems(removedElements, toTemp, part2=False):
    if part2:
        toFinal= toTemp + removedElements
    else:
        toFinal= toTemp + list(reversed(removedElements))
    return toFinal

def takeLastCranes(stackDict):
    result = ""
    for i in range(len(stackDict.keys())):
        result += stackDict[str(i+1)][-1]
    return result


# print(organizeCraneInfo())
# print(organizeMoves())

testDict = {'1': ['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'],
             '2': ['N', 'B', 'L'], 
             '3': ['J', 'C', 'H', 'T', 'L', 'V'], 
             '4': ['S', 'P', 'J', 'W'], 
             '5': ['Z', 'S', 'C', 'F', 'T', 'L', 'R'], 
             '6': ['W', 'D', 'G', 'B', 'H', 'N', 'Z'], 
             '7': ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'], 
             '8': ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'], 
             '9': ['R', 'P', 'M', 'L', 'H']}

testMove = ['move', '5', 'from', '3', 'to', '6']

# print(dealWithMove(testDict, testMove))


# submit(moveCranesAround(), part="a", day=5, year=2022)
# submit(moveCranesAround(part2=True), part="b", day=5, year=2022)