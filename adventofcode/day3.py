import utils
from aocd import submit

dataList = utils.readData(2022, 3,'\n')


def repeatedItem(items:list):
    result = set(items[0])
    otherItems = items[1:]
    for item in otherItems:
        result = result.intersection(set(item))
    (item, ) = result
    return item

def takeRepeatedType(string):
    half = len(string)//2
    firstHalf = string[:half]
    secondHalf = string[half:]
    repeatedElement = repeatedItem([firstHalf,secondHalf])
    return repeatedElement

def getRepeatedElements(dataList):
    repeatedElements = []
    for data in dataList:
        repeatedElements.append(takeRepeatedType(data))
    return repeatedElements

def createDictLetter():
    small_letters = list(map(chr, range(ord('a'), ord('z')+1)))
    big_letters = list(map(chr, range(ord('A'), ord('Z')+1)))
    letters = small_letters + big_letters
    value = 1
    letters_dict = {}
    for letter in letters:
        letters_dict[letter]=value
        value +=1
    return letters_dict

def calculateSumWithLetterWeight(letterList):
    letter_dict = createDictLetter()
    sum = 0
    for letter in letterList:
        sum += letter_dict[letter]
    return sum
    
def calculateResultPartA():
    repeatedElements = getRepeatedElements(dataList)
    return calculateSumWithLetterWeight(repeatedElements)

# plan:
# loop through the data every 3 items
# find common item for those 3 items - function
# find the priority add it to the sum  

def getAllRepeatedItems(dataList):
    # for each 3 items on the list get all repeated items
    i = 0 
    j = 3
    lastItem = len(dataList)
    repeatedLetters = []
    while j != lastItem:
        repeatedLetters.append(repeatedItem(dataList[i: j]))
        i = j 
        j = j + 3
    # adding the last 3 items
    repeatedLetters.append(repeatedItem(dataList[i:]))
  
    return repeatedLetters

def calculateResultPartB():
    repeatedElements = getAllRepeatedItems(dataList)
    return calculateSumWithLetterWeight(list(repeatedElements))

# test 
listExample = ['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg']
listExample1 = ['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']
print(repeatedItem(listExample)) # ---> {'r'}
print(repeatedItem(listExample1)) # ---> {Z}

testList = listExample + listExample1
print(getAllRepeatedItems(testList)) # ---> {'r','Z'}
print(getAllRepeatedItems(dataList)) # ---> {'r','Z'}

#submit(calculateResultPartA(), part="a", day=3, year=2022)
#submit(calculateResultPartB(), part="b", day=3, year=2022)