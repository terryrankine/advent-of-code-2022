from anytree import Node, RenderTree, Resolver
import testdata as td

rootRoot = Node('rootroot')
rootNode = Node('root', parent=rootRoot, files = {}, sumsize = 0)

currentPos = rootNode
curparent = rootNode.parent
currentAction = None

r = Resolver('name')

for line in td.data:
    if '$ cd /' in line:
        currentPos = rootNode
        curparent = rootNode.parent
        currentAction=None
    elif '$ ls' in line:
        currentAction = 'ls'
    elif '$ cd ..' in line:
        if currentPos.name == 'root':
            continue
        tempsize = currentPos.sumsize
        currentPos = currentPos.parent
        curparent = currentPos.parent
        currentAction=None
        currentPos.sumsize += tempsize
       

    elif currentAction == 'ls' and 'dir ' in line:
        name = line[4:].strip()
        tempNode = Node(name, parent=currentPos, files = {}, sumsize = 0)

    elif '$ cd ' in line:
        name = line[4:].strip()
        currentPos = r.get(currentPos, name)
        currentAction=None

    elif currentAction == 'ls':
        filesize, filename = line.split(' ')
        currentPos.files[filename]= int(filesize)
        tempsize = sum(currentPos.files.values())
        currentPos.sumsize = tempsize



print ('---------------')
size = 0
print(RenderTree(rootNode))


for currNode in rootRoot.descendants:
    if currNode.sumsize <= 100000:
        size +=currNode.sumsize
print (size)


sizes = []
for currNode in rootRoot.descendants:
    sizes.append(currNode.sumsize)

sizes = sorted(sizes)
currentUsed = sizes[-1]
for i in sorted(sizes):
    if 30000000 < 70000000-(currentUsed-i):
        print (i, 70000000-(currentUsed-i))
        break

