class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        tmp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = tmp.prev
            self.tail.next = None
            tmp.prev = None
        self.length -= 1
        return tmp
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        tmp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = tmp.next
            tmp.next = None
            self.head.prev = None
        self.length -= 1
        return tmp
        
    def printList(self):
        tmp = self.head
        print("-----------------")
        while tmp is not None:
            print(tmp.value, "- ", end="")
            tmp = tmp.next
        print("None")
        print("-----------------")
        print("length: ",self.length)
        if self.head is not None:
            print("head: ",self.head.value)
        else:
            print("head: ",self.head)
        if self.tail is not None:
            print("tail: ",self.tail.value)
        else:
            print("tail: ",self.tail)    
        
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.pop()
dll.pop()
dll.pop()
dll.prepend(1)
dll.prepend(0)
dll.append(2)
dll.pop_first()
dll.prepend(0)

dll.printList()
