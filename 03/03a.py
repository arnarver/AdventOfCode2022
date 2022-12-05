import string
file = open('input.txt', 'r+')
lines = [line.strip('\n') for line in file]

def createDict():
    lowerAlph = [chr(value) for value in range(ord('a'), ord('z') + 1)]
    upperAlph = [chr(value) for value in range(ord('A'), ord('Z') + 1)]
    dict = {}
    for char in lowerAlph:
        dict[char] = ord(char) - ord('a') + 1
    for char in upperAlph:
        dict[char] = ord(char) - ord('A') + 27
    return dict

def splitString(line):
    print(line)
    stringLength = int(len(line) / 2)
    print(stringLength)
    return ((set(list(line[0:stringLength])), set(list(line[stringLength:]))))

dict = createDict()

lines = [splitString(line) for line in lines]

def findDuplicate(tup):
    for x in tup[0]:
        if x in tup[1]:
            return x

dupes = [findDuplicate(line) for line in lines]

print(sum([dict[x] for x in dupes]))