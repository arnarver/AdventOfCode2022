# A ROCK
# B PAPER
# C SCISSORS
#
# X ROCK
# Y PAPER
# Z SCISSORS
#
# 1 ROCK
# 2 PAPER
# 3 SCISSORS 
#
# 0 LOSS
# 3 DRAW
# 6 WIN
file = open("input.txt", "+r")

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

LOSE_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6

def getSymbol(char):
    if(char == 'A' or char == 'X' ):
        return ROCK
    elif(char == 'B' or char =='Y'):
        return PAPER
    else: 
        return SCISSORS

def getOutcome(opponent, player):
    if((player == ROCK and opponent == SCISSORS) or (player == PAPER and opponent == ROCK) or(player == SCISSORS and opponent == PAPER)):
        return WIN_SCORE
    elif(player == opponent):
        return DRAW_SCORE
    else:
        return LOSE_SCORE

def getSymbolScore(symbol):
    if(symbol == ROCK):
        return 1
    elif(symbol == PAPER):
        return 2
    else: 
        return 3

def parseLine(line):
    return (getSymbol(line[0]), getSymbol(line[2]))
tuples = [parseLine(line)for line in file ]

scores = [getOutcome(x[0], x[1]) + getSymbolScore(x[1]) for x in tuples]
for line in scores:
    print(line)

score = sum(scores)
print(score)