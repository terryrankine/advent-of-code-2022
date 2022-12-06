from  testdata import *
import numpy as np
import pandas as pd
import regex as re


with open("stack.txt", 'w') as fp:
    fp.write(stack)

data = pd.read_fwf("stack.txt", colspecs='infer', header=None)

#back to native.... #declare space
stacks = [None] * (int(data.shape[0])+1)

#extract, remove null, reverse, make list (so end of list is 'top' of stack)
for i in data.columns:
    stacks[i]=data[i][~pd.isnull(data[i])][::-1].to_list()
    
for operation in operations: 
    move, fromstack, tostack = list(map(int,re.findall(r'\d+', operation)))
    for i in range (0,move):
        stacks[tostack-1].append(stacks[fromstack-1].pop())

for mystack in stacks:
    print (mystack.pop())

print('--------------')


#extract, remove null, reverse, make list (so end of list is 'top' of stack)
for i in data.columns:
    stacks[i]=data[i][~pd.isnull(data[i])][::-1].to_list()
print (stacks)

#part 2
tempstack = []
for operation in operations: 
    move, fromstack, tostack = list(map(int,re.findall(r'\d+', operation)))
    for i in range (0,move):
        tempstack.append(stacks[fromstack-1].pop())
    for i in range (0,len(tempstack)):
        stacks[tostack-1].append(tempstack.pop())

for mystack in stacks:
    try:
        print (mystack.pop())
    except:
        print("EMPTY")
