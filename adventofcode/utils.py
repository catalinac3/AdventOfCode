from aocd.models import Puzzle

def readData(year, day, splitBy):
    puzzle = Puzzle(year=year, day=day)
    dataList = puzzle.input_data.split(splitBy)
    return dataList
    