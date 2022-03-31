# MCP361 : Assignment 8
# Siddharth Dixit
# 2018ME20727

import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

print("Solution for Problem 1")
l = []
with open('MCP361_2018ME20727_Assignment8_Problem1.txt') as f:
    l = f.readlines()
d=[]
for line in l:
    d.append(line.replace("\n",""))
    
d = d[0].split(";")
for i in range(len(d)):
    d[i] = d[i].split(":")

f = []
for i in range(len(d)):
    temp = []
    n = int(d[i][0])
    temp.append(n)
    if d[i][1]==" ":
        temp.append(None)
    else:
        val = list(map(int, d[i][1].split(",")))
        temp.append(val)
    f.append(temp)

class TreeNode:
   def __init__(self, n, x):
       self.val = x
       self.left = None
       self.right = None
       self.node = n

def isEqual(a,b):
    if len(a)!=len(b):
        return False
    for i in range(len(a)):
        if a[i]!=b[i]:
            return False
    return True

Q = deque()
 
# Helper function helps us in adding data
# to the tree in Level Order
def insertValue(n, data, root):
    newnode = TreeNode(n, data)
    temp=None
    if Q:
        temp = Q[0]

    while (temp and temp.val):
        Q.popleft()
        temp=Q[0]

    if root == None:
        root = newnode

    # The left child of the current Node is
    # used if it is available.
    elif temp.left == None:
        if temp.val==None:
            temp.left = newnode
     
    # The right child of the current Node is used
    # if it is available. Since the left child of this
    # node has already been used, the Node is popped
    # from the queue after using its right child.
    elif temp.right == None:
        atemp = Q.popleft()
        if temp.val==None:
            temp.right = newnode
     
    # Whenever a new Node is added to the tree,
    # its address is pushed into the queue.
    # So that its children Nodes can be used later.
    Q.append(newnode)
    return root
 
def createTree(a, root):
    for i in range(len(a)):
        root = insertValue(a[i][0],a[i][1], root)
    return root
 
def levelOrder(root):
    Q = deque()
    Q.append(root)
    while Q:
        temp = Q.popleft()
        print(temp.node,temp.val, end = ' ')
        if temp.left != None:
            Q.append(temp.left)
        if temp.right != None:
            Q.append(temp.right)

root = None
root = createTree(f, root)
a = root
# levelOrder(root)
b=root

while(a.val==None):
    a=a.right

np = len(a.val)

def recur(root, player):
    if not root.left and not root.right:
        return
    if root.left and root.right:
        if root.left.val and root.right.val:
            op = max(root.left.val[player%np], root.right.val[player%np])
            if op == root.left.val[player%np]:
                root.val = root.left.val
            else:
                root.val = root.right.val
        elif root.left.val:
            recur(root.right, player+1)
        elif root.right.val:
            recur(root.left, player+1)
        else:
            recur(root.left, player+1)
            recur(root.right, player+1)
while(b.val==None):
    recur(b,0)
op = b.val
# levelOrder(b)
q=b
arr = []
prev = 0
while(True):
    if q.left==None and q.right==None:
        break
    if isEqual(op,q.left.val):
        q = q.left
        arr.append([prev, q.node])
        prev = q.node
    elif isEqual(op,q.right.val):
        q = q.right
        arr.append([prev, q.node])
        prev = q.node
# print()
# print(arr)
for a in range(len(arr)):
    print(f"At node {arr[a][0]} Player {a%np + 1} chooses to move to node {arr[a][1]}")
print(f"The backward induction strategy ends at node {arr[-1][1]}")
print("The optimal payoff vector is",op)
print()

G=nx.DiGraph()
for e in f:
    if not e[1]:
        G.add_node(e[0])
    else:
        G.add_node(e[0])
t = b
edges = []

def get_edges(t):
    global edges
    if t==None:
        return
    if t.left:
        temp = (t.node, t.left.node)
        edges.append(temp)
        get_edges(t.left)
    if t.right:
        temp = (t.node, t.right.node)
        edges.append(temp)
        get_edges(t.right)
get_edges(t)
for edge in edges:
    G.add_edge(*edge)
labels = {(0, 2): "Player 1", (2, 6):"Player 2", (2, 5): "Player 2", (0, 1):"Player 1", (1, 4):"Player 2", (1, 3):"Player 2"}
pos = nx.spring_layout(G)
nx.draw(G, pos,with_labels= True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_color='red')
p6 = pos[6]
p5 = pos[5]
p4 = pos[4]
p3 = pos[3]
plt.text(p6[0],p6[1]+0.1,s='(30,30)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
plt.text(p5[0],p5[1]+0.1,s='(100,20)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
plt.text(p4[0],p4[1]+0.1,s='(100,30)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
plt.text(p3[0],p3[1]+0.1,s='(40,50)', bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
plt.show()

for i in range(2,4):

    print(f"Solution For Problem {i}")

    l = []
    with open(f'MCP361_2018ME20727_Assignment8_Problem{i}.txt') as f:
        l = f.readlines()
    d=[]
    for line in l:
        d.append(line.replace("\n",""))
    
    d = d[0].split(";")
    for i in range(len(d)):
        d[i] = d[i].split(":")
    f = []
    for i in range(len(d)):
        temp = []
        n = int(d[i][0])
        temp.append(n)
        if d[i][1]==" ":
            temp.append(None)
        else:
            val = list(map(int, d[i][1].split(",")))
            temp.append(val)
        f.append(temp)

    Q = deque()

    root = None
    root = createTree(f, root)
    a = root
    b=root

    while(a.val==None):
        a=a.right

    np = len(a.val)

    while(b.val==None):
        recur(b,0)
    op = b.val
    q=b
    arr = []
    prev = 0
    while(True):
        if q.left==None and q.right==None:
            break
        if isEqual(op,q.left.val):
            q = q.left
            arr.append([prev, q.node])
            prev = q.node
        elif isEqual(op,q.right.val):
            q = q.right
            arr.append([prev, q.node])
            prev = q.node
    for a in range(len(arr)):
        print(f"At node {arr[a][0]} Player {a%np + 1} chooses to move to node {arr[a][1]}")
    print(f"The backward induction strategy ends at node {arr[-1][1]}")
    print("The optimal payoff vector is",op)
    print()







