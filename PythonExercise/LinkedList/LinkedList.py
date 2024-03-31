class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_code = Node(value)
        if self.length == 0:
            self.head = new_code
            self.tail = new_code
        else:
            self.tail.next = new_code
            self.tail = new_code
        self.length += 1
        return True
    
    def pop(self):
        tmp = self.head
        pre = self.head
        if self.length == 0 :
            return None
        while tmp.next is not None:
            pre = tmp
            tmp = tmp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tmp
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return tmp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bound")
            return None
        tmp = self.head
        for _ in range(0,index):
            tmp = tmp.next
        return tmp
    
    def set(self,index,value):
        tmp = self.get(index)
        if tmp is not None:
            tmp.value = value
            return True
        return False
        
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            print("Invalid index")
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        prev_node = self.get(index - 1)
        new_node = Node(value)
        tmp = prev_node.next
        prev_node.next = new_node
        new_node.next = tmp
        self.length += 1
        return True
    
    def reverse (self):
        tmp = self.head
        self.head = self.tail
        self.tail = tmp
        after = tmp.next
        before = None
        for _ in range(self.length):
            after = tmp.next
            tmp.next = before
            before = tmp
            tmp = after
            # if after.next: #last node.next is none, so it will cause error. have after assigned before moving tmp.next
            #     after = after.next
        return True
        
    
    def printList(self):
        list = []
        tmp = self.head
        while tmp is not None:
            list.append(tmp.value)
            tmp = tmp.next
        print(list)
        
    def printHead(self):
        if self.head is not None:
            print(self.head.value)
        else:
            print("Head: ","Empty Node")
        
    def printTail(self):
        if self.tail is not None:
            print(self.tail.value)
        else:
            print("Tail: ","Empty Node")
        
    def printTailNext(self):
        if self.tail.next is None:
            print("is none")
        else:
            print("is a node")
        
    def printLength(self):
        print(self.length)
    
my_ll = LinkedList(0)
my_ll.append(1)
my_ll.append(2)
my_ll.append(3)
my_ll.printList()

my_ll.reverse()
print("Reversed list")
my_ll.printList()

# my_ll.pop()
# my_ll.prepend(1)


print("--------------")

my_ll.printHead()
my_ll.printTail()
my_ll.printLength()