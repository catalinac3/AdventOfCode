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
    treesLookingDown = [organizedData[i][col] for i in range(0, row)]
    if max(treesLookingDown) < data:
        # is visible looking down
        return True
    
    
    treesLookingUp = [organizedData[i][col] for i in range(row + 1, len(organizedData))]
    if max(treesLookingUp) < data:
        # is visible looking up
        return True

   
    treesLookingRight = [organizedData[row][j] for j in range(0,col)]
    if max(treesLookingRight) < data:
        # is visible looking right
        return True

    
    treesLookingLeft = [organizedData[row][j] for j in range(col + 1, len(organizedData[0]))]
    if max(treesLookingLeft) < data:
        # is visible looking right
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

# Part B
# Best spot for a tree house

def calcScenicScore(data, row, col, organizedData):

    upScore = 0
    # iterate from tree to border
    for i in range(row - 1, -1,-1):
        if organizedData[i][col] < data:
            upScore += 1
        else:
            upScore += 1
            break    
    
    downScore = 0
    for i in range(row + 1, len(organizedData)):
        if organizedData[i][col] < data:
            downScore += 1
        else:
            downScore += 1
            break 
   
    leftScore = 0
    for j in range(col - 1,-1,-1):
        if organizedData[row][j] < data:
            leftScore += 1
        else:
            leftScore += 1
            break 

    rightScore = 0 
    for j in range(col + 1, len(organizedData[0])):
        if organizedData[row][j] < data:
            rightScore += 1
        else:
            rightScore += 1
            break 

    if data == str(5):   
        print(f'data {data}, row {row}, column {col}')
        print(f'downScore {downScore}, upScore {upScore}, rightScore {rightScore}, leftScore {leftScore}')
        print(f'scenic score {downScore * upScore * rightScore * leftScore}')

    return downScore * upScore * rightScore * leftScore


def maxScenicScore(organizedData):
    endRow = len(organizedData) 
    endColumn = len(organizedData[0]) 
   
    maximumScenicScore = 0
    # iterate through all trees
    for i in range(0, endRow):
        for j in range(0, endColumn):
            newScenicScore = calcScenicScore(organizedData[i][j], i, j, organizedData)
            if newScenicScore > maximumScenicScore:
                maximumScenicScore = newScenicScore   
    return maximumScenicScore

def highestScenicScore(dataList):
    organizedData = organizeData(dataList)
    maximumScenicScore = maxScenicScore(organizedData)
    return maximumScenicScore


# print(highestScenicScore(data_example))
print(highestScenicScore(dataList))