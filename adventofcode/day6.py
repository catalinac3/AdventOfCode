import utils
from aocd import submit

data = utils.readSimpleData(2022, 6)

charList = utils.splitStringIntoListOfChars(data)

# print(charList)

def calculateFirstMarker(charList):
    i=0
    j=4
    foundMarker = False
    while j < (len(charList)-1) or foundMarker:
        temp = charList[i:j]
        if checkIfDigitsAreDifferent(temp):
            foundMarker = True
            marker = j
            return marker
        i+=1
        j+=1
        

def calculateFirstMarkerPartB(charList):
    i=0
    j=14
    foundMarker = False
    while j < (len(charList)-1) or foundMarker:
        temp = charList[i:j]
        if checkIf14DigitsAreDifferent(temp):
            foundMarker = True
            marker = j
            return marker
        i+=1
        j+=1
 
    
    
def checkIfDigitsAreDifferent(listOfFour):
    return len(set(listOfFour)) == 4

def checkIf14DigitsAreDifferent(listOfFourteen):
    return len(set(listOfFourteen)) == 14


# print(checkIfDigitsAreDifferent(['l', 'q', 's', 'm'])) #---> True
# print(checkIfDigitsAreDifferent(['l', 'q', 'q', 'm'])) # ----> False'

testString = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
charListTest = utils.splitStringIntoListOfChars(testString)
print(calculateFirstMarker(charListTest)) # ----> 5

testString2 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
charListTest2 = utils.splitStringIntoListOfChars(testString2)
print(calculateFirstMarkerPartB(charListTest2)) # ----> 19

print(calculateFirstMarker(charList)) # ----> 5
print(calculateFirstMarkerPartB(charList))