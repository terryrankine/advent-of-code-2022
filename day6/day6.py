#sliding window....
import testdata

#tests
for checkme in testdata.tests:
    print (checkme)
    for i in range(1,len(checkme)):
        if len(set(checkme[i:i+4])) == 4:
            print(i+4)
            print('-------')
            break

#part1
for i in range(1,len(testdata.actual)):
    if len(set(testdata.actual[i:i+4])) == 4:
        print(i+4)
        break

#part1
for i in range(1,len(testdata.actual)):
    if len(set(testdata.actual[i:i+14])) == 14:
        print(i+14)
        break