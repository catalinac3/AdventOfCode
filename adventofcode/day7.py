import utils
from aocd import submit

dataList = utils.readData(2022, 7, "\n")
dataListExample = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.split('\n')


def handlesChangeDir(command, path, sizeDir):
    dir = command.replace('$ cd', '').strip()
    if dir == '/':
        path = ['/root']
    elif dir == '..':
        path.pop()
    else:
        newPath = f"/{dir}"
        path.append(newPath)
        #create a new key in the dict and set it to 0 if it doesn't exists
        stringPath = "".join(path)
        sizeDir[stringPath] = sizeDir.get(stringPath, 0)
    return path
   

def calculateDirsSize(dataList):
    path = []
    sizeDir = {"/root": 0}
    for data in dataList:
        # It is a command to alter path -- change directory
        if data.startswith("$ cd"):
            path = handlesChangeDir(data, path, sizeDir)

        if not data.startswith("$") and not data.startswith("dir"):
            file = data.split(" ")
            # add file size to directories that contain this file
            addFileToRelatedPaths(path, sizeDir, file)
    return sizeDir

def addFileToRelatedPaths(path, sizeDir, file):
    stringPath = ""
    for dir in path:
        stringPath += dir
        sizeDir[stringPath] += int(file[0])


def calcSumAllUnder100000(dataListExample):
    sizeDir = calculateDirsSize(dataListExample)
    sum = 0
    for _, value in sizeDir.items():
        if value <= 100000:
            sum+= value
    return sum

def identifyFile(sizeDir, neededFreeSpace):
    smallest = sizeDir['/root']
    filePath = '/root'
    for path , size in sizeDir.items():
        if size >= neededFreeSpace:
            if size < smallest:
                smallest = size
                filePath = path
    print(f'smallest {smallest}, file {filePath}')
    return smallest

# print(calcSumAllUnder100000(dataListExample)) # ----> 95437
# print(calcSumAllUnder100000(dataList)) 

def identifyFileToErase(dataList):
    sizeDir = calculateDirsSize(dataList)
    updateRequirement = 30000000
    totalDiskAvailable = 70000000
    freeSpace = totalDiskAvailable - sizeDir['/root'] # 25204323
    neededFreeSpace = updateRequirement - freeSpace # 4795677
    smallest = identifyFile(sizeDir, neededFreeSpace)
    return smallest

print(identifyFileToErase(dataList))