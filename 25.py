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

def kth_to_last_node(k, head_of_list):
    scout = head_of_list
    seeker = head_of_list
    lead = 0;

    while(scout != None and lead < k):
        scout = scout.next
        lead += 1

    if(k > lead and scout == None):
        return "Invalid K Value, list too short"

    while(scout != None):
        scout = scout.next
        seeker = seeker.next

    return seeker.value

    

def test():
    linkedList = LinkedList()

    linkedList.add("Eccles")
    linkedList.add("Devil's Food")
    linkedList.add("Cheese")
    linkedList.add("Bundt")
    linkedList.add("Angel Food")

    print(kth_to_last_node(2, linkedList.head))

def test2():
    linkedList = LinkedList()

    linkedList.add("Eccles")
    linkedList.add("Devil's Food")
    linkedList.add("Cheese")
    linkedList.add("Bundt")
    linkedList.add("Angel Food")

    print(kth_to_last_node(7, linkedList.head))

def test3():
    linkedList = LinkedList()

    linkedList.add("Eccles")

    print(kth_to_last_node(1, linkedList.head))

def test4():
    linkedList = LinkedList()

    linkedList.add("Eccles")
    linkedList.add("Devil's Food")

    print(kth_to_last_node(2, linkedList.head))

def test5():
    linkedList = LinkedList()

    print(kth_to_last_node(2, linkedList.head))

test()
test2()
test3()
test4()
test5()
    
