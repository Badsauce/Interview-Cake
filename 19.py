class stackQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self,item):
        self.in_stack.append(item)

    def pop(self):
        if len(self.out_stack) <= 0:
            self._dump_in_stack()
            if len(self.out_stack) <= 0:
                return False
        return self.out_stack.pop()

    def _dump_in_stack(self):
        while(len(self.in_stack) > 0):
            self.out_stack.append(self.in_stack.pop())

def insert(queue,input_item):
    print("inserting {} into queue".format(input_item))
    queue.push(input_item)

def pop(queue):
    print("popped {} off the queue".format(queue.pop()))

test_stack = stackQueue()



insert(test_stack,3)
insert(test_stack,2)
insert(test_stack,90)
insert(test_stack,7)
insert(test_stack,2)
insert(test_stack,6)

pop(test_stack)
pop(test_stack)
pop(test_stack)
pop(test_stack)
pop(test_stack)
pop(test_stack)
