from aocd.models import Puzzle
from aocd import submit

puzzle = Puzzle(year=2022, day=1)
elfenCaloriesList = puzzle.input_data.split('\n\n')

elfenSumList = []
for elf in elfenCaloriesList:
    elfList = elf.split('\n')
    elfCal = [int(x) for x in elfList]
    elfenSumList.append(sum(elfCal))    

# submit(max(elfenSumList), part="a", day=1, year=2022)
# submit(sum(sorted(elfenSumList, reverse=True)[0:3]), part="b", day=1, year=2022)
