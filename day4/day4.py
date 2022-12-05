from testdata import *
import re

data = data1

count=0
r1min, r1max, r2min, r2max = 0,0,0,0
for line in data:
    r1min, r1max, r2min, r2max = list(map(int, re.findall('\d+',line)))
   
    if r1min<=r2min and r1max>=r2max:
        print ('first range wider', r1min, r1max, r2min, r2max)
        count+=1
    elif r1min>=r2min and r1max<=r2max:
        print ('second range wider', r1min, r1max, r2min, r2max)
        count +=1
        
print (count)

count=0
r1min, r1max, r2min, r2max = 0,0,0,0
for line in data:
    r1min, r1max, r2min, r2max = list(map(int, re.findall('\d+',line)))
   
    if r1min<=r2min and r2min<=r1max:
        print ('first partoverlap', r1min, r1max, r2min, r2max)
        count+=1
    elif r2min<=r1min and r1min<=r2max:
        print ('second part wider', r1min, r1max, r2min, r2max)
        count +=1
        
print (count)