import utils
from aocd import submit

dataList = utils.readData(2022, 4,'\n')
# In how many assignment pairs does one range fully contain the other?
def howManyPairs(dataList):
    countAssigments = 0
    for data in dataList:
        # divide the data into a list of pairs
        pair1, pair2 = data.split(",")
        # make for each pair a set with the cover numbers
        set1 = makePairASet(pair1)
        set2 = makePairASet(pair2)
        # find out if one set contains the other with isSubset()
        if oneContainsTheOther(set1, set2):
            countAssigments +=1
    return countAssigments
          

def makePairASet(pair):
    pairRange = pair.split("-")
    resultSet = set()
    fromNumber = int(pairRange[0])
    toNumber = int(pairRange[1]) + 1
    for i in range(fromNumber, toNumber):
        resultSet.add(i)
    return resultSet

def oneContainsTheOther(set1, set2):
    if set1.issubset(set2) or set2.issubset(set1):
        return True
    return False

def doSetsOverlap(set1, set2):
    intersectionSet = set1.intersection(set2)
    if len(intersectionSet) > 0:
        return True
    return False



#In how many assignment pairs do the ranges overlap?
def howManyPairsOverlap(dataList):
    countAssigments = 0
    for data in dataList:
        # divide the data into a list of pairs
        pair1, pair2 = data.split(",")
        # make for each pair a set with the cover numbers
        set1 = makePairASet(pair1)
        set2 = makePairASet(pair2)
        # find out if one set contains the other with isSubset()
        if doSetsOverlap(set1, set2):
            countAssigments +=1
    return countAssigments


submit(howManyPairs(dataList), part="a", day=4, year=2022)
submit(howManyPairsOverlap(dataList), part="b", day=4, year=2022)