from aocd.models import Puzzle
from aocd import submit

from day1 import readData 

# score:
# rock defeats scissors
# scissors defeat paper
# paper defeats rock

# A ---> rock -- points: 1
# B ---> paper -- points: 2
# C ---> scissors -- points: 3

# a)
# X for rock
# Y for paper 
# Z for scissors

# 0 lost
# 3 draw
# 6 won
pointsGameOutcomeA = {
        ("A", "X"):3 ,  ("A", "Y"):6 , ("A", "Z"):0,
        ("B", "X"):0 ,  ("B", "Y"):3 , ("B", "Z"):6 ,
        ("C", "X"):6 ,  ("C", "Y"):0 , ("C", "Z"):3
    }

pointsFormSelectedA = {
        "X":1, # rock 
        "Y":2, # paper
        "Z":3, # scissors
    }


def pointsSumA(dataList, pointsFormSelected, pointsGameOutcome):
    pointsSumA = 0
    for data in dataList:
        game = tuple(data.split())
        pointsSumA += pointsFormSelected.get(game[1])
        pointsSumA += pointsGameOutcome.get(game)
    return pointsSumA
    
# b)

# shape selected
rock = 1 #A #X
paper = 2 #B #Y
scissors = 3 #C #Z

lost = 0
draw = 3
won = 6

# X means you need to lose
# Y means it should be draw
# Z you need to win
# you need to calculate which shape to choose

pointsGameOutcomeB = {
        "X":0, # rock 
        "Y":3, # paper
        "Z":6, # scissors
    }

pointsFormSelectedB = {
        ("A", "X"): 3,  ("A", "Y"):1 , ("A", "Z"):2,
        ("B", "X"): 1 ,  ("B", "Y"):2 , ("B", "Z"):3,
        ("C", "X"):2 ,  ("C", "Y"):3 , ("C", "Z"):1
    }

def pointsSumB(dataList, pointsGameOutCome, pointsForm):
    pointsSumB = 0
    for data in dataList:
        game = tuple(data.split())
        pointsSumB += pointsGameOutCome.get(game[1])
        pointsSumB += pointsForm.get(game)
    print(pointsSumB)
    return pointsSumB


dataList = readData(2022, 2,'\n')
#submit(pointsSumA(dataList, pointsFormSelectedA, pointsGameOutcomeA), part="a", day=2, year=2022)
submit(pointsSumB(dataList,pointsGameOutcomeB, pointsFormSelectedB), part="b", day=2, year=2022)
