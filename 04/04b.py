file = open('input.txt', 'r+')


def splitLine(line):
    a, b = line.strip('\n').split(',')
    a, b = (tuple(a.split('-')), tuple(b.split('-')))
    return (int(a[0]), int(a[1])), (int(b[0]), int(b[1]))


count = 0

for line in file:
    a, b = splitLine(line)
    # if(a[0] > b[1] or a[1] < b[0]):
    #    continue
    aRange = range(a[0], a[1]+1)
    bRange = range(b[0], b[1]+1)
    # print(numberRange)
    if(b[0] in aRange or b[1] in aRange or a[0] in bRange or a[1] in bRange):
        count = count + 1
    else:
        print(a, b)

print(count)
