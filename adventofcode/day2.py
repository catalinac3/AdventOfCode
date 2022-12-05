from aocd.models import Puzzle
from aocd import submit

puzzle = Puzzle(year=2022, day=2)
rockPaperScissorList = puzzle.input_data.split('\n')
print(rockPaperScissorList)

scores = {
        ("A", "X"):3 ,  ("A", "Y"):6 , ("A", "Z"):0,
        ("B", "X"):0 ,  ("B", "Y"):3 , ("B", "Z"):6 ,
        ("C", "X"):6 ,  ("C", "Y"):0 , ("C", "Z"):3
    }

pointsSelected = {
        "X":1,
        "Y":2,
        "Z":3,
    }

sum = 0
for rockPaperScissor in rockPaperScissorList:
    game = tuple(rockPaperScissor.split())
    sum += pointsSelected.get(game[1])
    sum += scores.get(game)
    
#submit(sum, part="a", day=2, year=2022)

# shape selected
rock = 1 #A #X
paper = 2 #B #Y
scissors = 3 #C #Z

# score
# rock defeats scissors
# scissors defeat paper
# paper defeats rock

lost = 0
draw = 3
won = 6