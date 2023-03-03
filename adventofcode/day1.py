from aocd import submit
import utils


elfenCaloriesList = utils.readData(2022, 1,'\n\n')

elfenSumList = []
for elf in elfenCaloriesList:
    elfList = elf.split('\n')
    elfCal = [int(x) for x in elfList]
    elfenSumList.append(sum(elfCal))    

# submit(max(elfenSumList), part="a", day=1, year=2022)
# submit(sum(sorted(elfenSumList, reverse=True)[0:3]), part="b", day=1, year=2022)
