class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

def buildTree(table):
    treeHead = Node(table[0])
    stack = [treeHead]
    table = table[1:]
    while stack:
        elem = stack[0]
        if table:
            leftNode = Node(table[0])
            elem.setLeft(leftNode)
            table = table[1:]
            stack.append(leftNode)
        if table:
            rightNode = Node(table[0])
            elem.setRight(rightNode)
            table = table[1:]
            stack.append(rightNode)
        stack = stack[1:]
    return treeHead

def isMaxHeap(heapHead):
    pass

def adjusteMaxHeapNode(heapNode):
    if not heapNode.left and heapNode.right:
        max, side = heapNode.right.value, "right"
    elif not heapNode.right and heapNode.left:
        max, side = heapNode.left.value, "left"
    elif not heapNode.right and not heapNode.left:
        max, side = -2147483647, "None"
    max, side = heapNode.left.value, "left" if heapNode.left.value > heapNode.right.value else heapNode.right.value, "right"
    if max > heapNode.value:
        if side == "left":
            heapNode.left.value = heapNode.value
            heapNode.value = max
        elif side =="right":
            heapNode.right.value = heapNode.value
            heapNode.value = max
    return heapNode

def buildMaxHeap(heapHead):
    heapHead = adjusteMaxHeapNode(heapHead)
    # If left recursive on left
    # If right recursive on right
    # then readjuste HeapNode

def heapsort(table):
    tree = buildTree(table)
