import utils
from aocd import submit

dataList = utils.readData(2022, 3,'\n')

def takeRepeatedType(string):
    half = len(string)//2
    firstHalf = string[:half]
    secondHalf = string[half:]
    repeatedElement = list(set(firstHalf).intersection(set(secondHalf)))[0]
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

letter_dict = createDictLetter()

def calculateResult():
    repeatedElements = getRepeatedElements(dataList)
    letter_dict = createDictLetter()
    sum = 0
    for letter in repeatedElements:
        sum += letter_dict[letter]
    return sum