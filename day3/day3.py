from dataFile import *

def theScore(charInbound):
    if charInbound.isupper():
        return(ord(charInbound)-38)
    else:
        return(ord(charInbound)-96)

total = 0
for currentLine in data:
    commonChar = ''.join(set(currentLine[:len(currentLine)//2]).intersection(currentLine[len(currentLine)//2:]))
    total += theScore(commonChar)
print (total)


total = 0
prevSet = {}
for idx, currentLine in enumerate(data):
    commonChar = (set(currentLine))
    if idx % 3 == 0:
        prevSet = commonChar
    else: 
        prevSet = prevSet.intersection(commonChar)
    
    if idx % 3 == 2:
        #3rdtimes a charm....
        commonChar = ''.join(prevSet)
        total += theScore(commonChar)
        prevSet = {}

print (total)