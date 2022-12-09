import numpy as np
import testdata as td
import math

np.set_printoptions(threshold=np.inf)
np.set_printoptions(edgeitems=10,linewidth=180)

matsize = 400
startingpos = matsize//2

coverage = np.zeros((matsize,matsize))

headpos=(startingpos,startingpos)
tailpos=(startingpos,startingpos)

coverage[startingpos][startingpos] = 1

snakebody=[(startingpos,startingpos)]*10


def movehead(direction, myheadpos):
    if direction == 'U':
        myheadpos = (myheadpos[0]-1, myheadpos[1])
    if direction == 'D':
        myheadpos = (myheadpos[0]+1, myheadpos[1])
    if direction == 'L':
        myheadpos = (myheadpos[0], myheadpos[1]-1)
    if direction == 'R':
        myheadpos = (myheadpos[0], myheadpos[1]+1)
    return myheadpos

def movetail(mytailpos, myheadpos):
    if myheadpos[0]>mytailpos[0]:
        mytailpos=(mytailpos[0]+1, mytailpos[1])
    if myheadpos[0]<mytailpos[0]:
        mytailpos=(mytailpos[0]-1, mytailpos[1])
   
    if myheadpos[1]>mytailpos[1]:
        mytailpos=(mytailpos[0], mytailpos[1]+1)
    if myheadpos[1]<mytailpos[1]:
        mytailpos=(mytailpos[0], mytailpos[1]-1)
    return mytailpos
    
        

#part1
for moves in td.instructions:
    for i in range(1,int(moves[2:])+1):
        #move head
        direction = moves[0]
        headpos = movehead(direction, headpos)
        distance = (math.sqrt((headpos[0]-tailpos[0])**2+(headpos[1]-tailpos[1])**2))

        if distance >= 2:
            tailpos = movetail(tailpos, headpos)

        coverage[tailpos] = -1   

print(np.count_nonzero(coverage))


#part2
coverage = np.zeros((matsize,matsize))
coverage[startingpos][startingpos] = 1

for moves in td.instructions:
    for i in range(1,int(moves[2:])+1):
        for bodypart in range(9):
            headpos = snakebody[bodypart]
            tailpos = snakebody[bodypart+1]
            #move head
            direction = moves[0]
            if bodypart == 0:
                headpos = movehead(direction, headpos)
            
            distance = (math.sqrt((headpos[0]-tailpos[0])**2+(headpos[1]-tailpos[1])**2))

            if distance >= 2:
                tailpos = movetail(tailpos, headpos)
            snakebody[bodypart] = headpos
            snakebody[bodypart+1] = tailpos
        coverage[snakebody[9]] = -1

print(np.count_nonzero(coverage))

