file = open("input.txt", "+r")
list = []
counter = 0
sum = 0
largestSum = 0
largestCounter = 0
for line in file:
    #if(int(line) > 0):
    #    sum = sum + int(line)
    if(line == '\n'):
        list.append(sum)
        if(sum > largestSum):
            largestSum = sum
            largestCounter = counter
        sum = 0
        counter = counter + 1
    else:
        sum = sum + int(line)

print(largestSum, largestCounter)

list.sort(reverse=True)

print(list[0]+list[1]+list[2])