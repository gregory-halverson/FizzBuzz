__author__ = 'gregory'

import sys

filename = sys.argv[1]

sets = []

with open(filename) as f:
    for line in f:
        set = line.split()
        sets.append(set)

for set in sets:
    output = ''

    fizz = int(set[0])
    buzz = int(set[1])
    limit = int(set[2])

    for i in range(1, limit + 1):
        if not i % fizz and not i % buzz:
            output += 'FB '
        elif not i % fizz:
            output += 'F '
        elif not i % buzz:
            output += 'B '
        else:
            output += str(i) + ' '

    print(output)