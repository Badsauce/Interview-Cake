class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        newNode = LinkedListNode(value)
        newNode.next = self.head
        self.head = newNode

    def display(self):
        pointer = self.head
        while pointer != None:
            print('[',pointer.value,']', sep='')
            pointer = pointer.next

    def reverse(self):
        previous_node = None
        current_node = self.head
        next_node = None
        while current_node != None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
            

def test():
    print('Test 1: reverse a simple list')
    linkedList = LinkedList()

    linkedList.add(1)
    linkedList.add(2)
    linkedList.add(3)
    linkedList.add(4)
    
    linkedList.display()

    linkedList.reverse()

    linkedList.display()

def test2():
    print('Test 2: reverse an empty list')
    linkedList = LinkedList()
    
    linkedList.display()

    linkedList.reverse()

    linkedList.display()

def test3():
    print('Test 2: reverse a single element list')
    linkedList = LinkedList()

    linkedList.add(1)
    
    linkedList.display()

    linkedList.reverse()

    linkedList.display()

test()
test2()
test3()
