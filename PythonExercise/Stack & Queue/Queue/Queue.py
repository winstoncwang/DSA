class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.first is None:
            return None
        tmp = self.first
        self.first = self.first.next
        tmp.next = None
        self.length -= 1
        if self.length == 0:
            self.last = None
        return tmp
        
    def printQueue(self):
        tmp = self.first
        while tmp is not None:
            print(tmp.value, "- ", end="",)
            tmp = tmp.next
        print("self.first: ", self.first)
        print("self.last: ", self.last)
        print("self.length: ", self.length)
        return
    
    
queue = Queue(1)

queue.enqueue(2)
queue.enqueue(3)
queue.printQueue()
print("-------------")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.printQueue()