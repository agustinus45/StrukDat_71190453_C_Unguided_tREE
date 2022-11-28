class Node:
    def __init__(self,data,parent):
        self._data = data
        self._children = []
        self._parent = parent

    def addChild(self,data):
        self._children.append(data)

    def depth(node):
        if node.isRoot():
            return 0;
        else:
            return 1+depth(node.parent())

    def height(node):
        if node.isExternal():
            return 0
        else:
            h = 0
            for i in node.children():
                h = max(h, height(i))
            return 1+h


root = Node(200,None)
a=Node(23,root)
b=Node(11,root)
c=Node(13,a)
d=Node(57,a)
f=Node(32,b)
g=Node(42,c)
h=Node(51,c)
i=Node(71,c)
j=Node(12,d)
k=Node(15,d)
l=Node(33,f)
m=Node(8,f)

a.addChild(c)
a.addChild(d)
b.addChild(f)
c.addChild(g)
c.addChild(h)
c.addChild(i)
d.addChild(j)
d.addChild(k)
f.addChild(l)
f.addChild(m)
root.addChild(a)
root.addChild(b)