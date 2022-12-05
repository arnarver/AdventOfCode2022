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


dict = createDict()

def convertStringToSet(line): 
    return set(list(line))
groups = [(convertStringToSet(lines[x]), convertStringToSet(lines[x+1]), convertStringToSet(lines[x+2])) for x in range(0, len(lines), 3)]

def findBadge(group):
    for char in group[0]:
        if(char in group[1] and char in group[2]):
            return char

badges = [findBadge(group) for group in groups]

print(sum(dict[x] for x in badges))