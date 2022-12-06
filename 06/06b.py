file = open('input.txt', 'r+')
string = file.readline()

def findIndex(string):
    for i in range(0, len(string)-13):
        chars = set(string[i:i+14])
        if len(chars) == 14:
            return i+14


print(findIndex(string))
