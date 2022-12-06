from collections import deque
file = open('input.txt', 'r+')
stacks = [deque() for x in range(0, 9)]
stackInput = [file.readline() for x in range(0, 8)]
print(file.readline())
print(file.readline())

# print(stackInput)
print(len(stackInput))
for x in range(len(stackInput)-1, -1, -1):
    for index in range(0, len(stackInput[x])):
        if(stackInput[x][index].isalpha()):
            stackNumber = int(index / 4)
            stacks[stackNumber].append(stackInput[x][index])



lines = file.readlines()


def parseMove(line):
    strings = line.strip('\n').split(' ')
    return int(strings[1]), int(strings[3]) - 1, int(strings[5]) - 1


moves = [parseMove(line) for line in lines]


def makeMove(move):
    counter, takeFrom, moveTo = move
    for x in range(0, counter):
        value = stacks[takeFrom].pop()
        stacks[moveTo].append(value)

for move in moves:
    makeMove(move)

for x in stacks:
    print(x)

print(''.join([x.pop() for x in stacks]))