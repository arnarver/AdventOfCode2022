# A ROCK
# B PAPER
# C SCISSORS
#
# X LOSE
# Y DRAW
# Z WIN
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

LOSE = 'LOSE'
DRAW = 'DRAW'
WIN = 'WIN'

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

LOSE_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6


def getSymbol(char):
    if(char == 'A'):
        return ROCK
    elif(char == 'B'):
        return PAPER
    else:
        return SCISSORS


def getOutcome(outcome):
    if(outcome == 'X'):
        return LOSE
    elif(outcome == 'Y'):
        return DRAW
    else:
        return WIN


def getPlayerSymbol(opponent, outcome):
    if((opponent == ROCK and outcome == LOSE) or (opponent == SCISSORS and outcome == DRAW) or (opponent == PAPER and outcome == WIN)):
        return SCISSORS
    elif((opponent == PAPER and outcome == LOSE) or (opponent == ROCK and outcome == DRAW) or (opponent == SCISSORS and outcome == WIN)):
        return ROCK
    else:
        return PAPER


def getSymbolScore(symbol):
    if(symbol == ROCK):
        return 1
    elif(symbol == PAPER):
        return 2
    else:
        return 3

def getOutcomeScore(outcome):
    if(outcome == LOSE):
        return LOSE_SCORE
    elif(outcome == DRAW):
        return DRAW_SCORE
    else:
        return WIN_SCORE

def parseLine(line):
    return (getSymbol(line[0]), getOutcome(line[2]))


tuples = [parseLine(line)for line in file]

scores = [getSymbolScore(getPlayerSymbol(x[0], x[1])) + getOutcomeScore(x[1]) for x in tuples]
for line in tuples:
    print(line)

score = sum(scores)
print(score)
