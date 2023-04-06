from aocd.models import Puzzle

def readData(year, day, splitBy):
    puzzle = Puzzle(year=year, day=day)
    dataList = puzzle.input_data.split(splitBy)
    return dataList

def readSimpleData(year, day):
    puzzle = Puzzle(year=year, day=day)
    data = str(puzzle.input_data)
    return data
    
def splitStringIntoListOfChars(string):
    charList = [x for x in string] 
    return charList