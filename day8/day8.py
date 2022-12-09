import testdata as td
import numpy as np

import sys
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=np.inf)

maxView = 0
sizer = len(td.sample)
data = np.zeros((len(td.sample),len(td.sample))).astype(int)
trees = np.copy(data)
for row in range(len(td.sample)):
    data[row] = np.asarray(list(x for x in td.sample[row]))

maxL = -1
maxR = -1
seen = []

for idxr, row in enumerate(data):
    for idxc, i in enumerate(row):
        if (i > maxL):
            maxL=i
            seen.append([idxr, idxc])
    for idxc, i in enumerate(row[::-1]):
        if (i > maxR):
            maxR=i
            seen.append([idxr, sizer-1-idxc])
    maxL=-1
    maxR=-1

for idxc, col in enumerate(data.T):
    for idxr, i in enumerate(col):
        if (i > maxL):
            maxL=i
            seen.append([idxr, idxc])
    for idxr, i in enumerate(col[::-1]):
        if (i > maxR):
            maxR=i
            seen.append([sizer-1-idxr, idxc])
    maxL=-1
    maxR=-1

#my beautiful forrest.....
for i in sorted(seen):
    trees[i[0]][i[1]] = 1

#dupes
print(len(seen))

#nodupes
print(np.count_nonzero(trees))


#part 2
def dist_to_next(cell, array):
    count = 0
    mynum = array[cell]
    if cell >= len(array)-1:
        return count
    while True:
        count+=1
        cell+=1
        if (cell >= len(array)-1) or (mynum <= array[cell]):
            break
    return count

def dist_to_prev(cell, array):
    count = 0
    mynum = array[cell]
    while True:
        count+=1
        cell-=1
        if cell<=0 or mynum <= array[cell]:
            break
    return count



for i in seen:
    row, col = i
    if row == 0 or col == 0 or row == len(data)-1 or col == len(data)-1:
        continue
    calc = dist_to_next(row,data[:,col])* dist_to_prev(row,data[:,col])* dist_to_next(col,data[row,:])* dist_to_prev(col,data[row,:])
    if calc > maxView:
        maxView=calc

print (maxView)