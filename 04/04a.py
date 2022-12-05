file = open('input.txt', 'r+')

def splitLine(line):
    a, b = line.strip('\n').split(',')
    a, b = (tuple(a.split('-')), tuple(b.split('-')))
    return (int(a[0]), int(a[1])), (int(b[0]), int(b[1]))

count = 0
for line in file:
    a, b = splitLine(line)
    if((a[0] >= b[0] and a[1] <= b[1]) or (b[0]>= a[0] and b[1] <= a[1])):
        count = count + 1

print(count)