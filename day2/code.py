from dataFile import *

def human(line):
    line = line.replace('A', 'Rock')
    line = line.replace('B', 'Paper')
    line = line.replace('C', 'Scissors')
    line = line.replace('X', 'Rock')
    line = line.replace('Y', 'Paper')
    line = line.replace('Z', 'Scissors')
    return line    

def human2(line):
    line = line.replace('A', 'Rock')
    line = line.replace('B', 'Paper')
    line = line.replace('C', 'Scissors')
    line = line.replace('X', 'Lose')
    line = line.replace('Y', 'Draw')
    line = line.replace('Z', 'Win')
    return line   


print(data[:20])
total = 0
for line in data:
    if line in wins:
        total += 6
        total += score[line[2]]
    elif line in draws:
        total += 3
        total += score[line[2]]
    else:
        total += score[line[2]]
print (total)

total = 0
for line in data:
    if line[2] == 'X':
        #loosing
        total += 0
        total += score[loosing[line[0]]]
    elif line[2] == 'Y':
        #draw
        total += 3
        total += score[drawing[line[0]]]
    else:
        #winning
        total += 6
        total += score[winning[line[0]]]
print (total)
