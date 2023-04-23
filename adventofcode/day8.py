import utils
forest_example = '''30373
25512
65332
33549
35390'''

# Each tree is represented as a single digit whose value is its height, 
# where 0 is the shortest and 9 is the tallest.

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
dataList = utils.readData(2022, 8, "\n")

data_example = forest_example.split('\n')

def organizeData(dataList):
    organizedData = []
    for data in dataList:
        charList = utils.splitStringIntoListOfChars(data)
        organizedData.append(charList)
    return organizedData

def calculateVisibleBorders(organizedData):
    rows = len(organizedData)
    columns = len(organizedData[0])
    return rows * 2 + (columns - 2) * 2

def isVisible(data, row, col, organizedData):
    visibleLookDown = True
    for i in range(0, row):
        if organizedData[i][col] >= data:
            visibleLookDown = False

    if visibleLookDown:
        return True
    
    visibleLookUp = True
    for i in range(row + 1, len(organizedData)):
        if organizedData[i][col] >= data:
            visibleLookUp = False

    if visibleLookUp:
        return True
   
    visibleLookRight = True
    for j in range(0,col):
        if organizedData[row][j] >= data:
            visibleLookRight = False

    if visibleLookRight:
        return True

    visibleLookLeft = True
    for j in range(col + 1, len(organizedData[0])):
        if organizedData[row][j] >= data:
            visibleLookLeft = False

    if visibleLookLeft:
        return True
        
    return False


def calculateVisibleInnerTrees(organizedData):
    startRow = 1
    startColumn = 1
    endRow = len(organizedData) - 1
    endColumn = len(organizedData[0]) -1
    visible = 0

    # iterate through the inner trees
    for i in range(startRow, endRow):
        for j in range(startColumn, endColumn):
            if isVisible(organizedData[i][j], i, j, organizedData):
                visible += 1
    return visible

def findVisible(dataList):
    organizedData = organizeData(dataList)
    visibleBorders = calculateVisibleBorders(organizedData)
    visibleInnerTress = calculateVisibleInnerTrees(organizedData)
    return visibleBorders + visibleInnerTress


