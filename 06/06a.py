file = open('input.txt', 'r+')
string = file.readline()

def findIndex(string):
    for i in range(0, len(string)-3):
        chars = set(string[i:i+4])
        if len(chars) == 4:
            return i+4


print(findIndex(string))
