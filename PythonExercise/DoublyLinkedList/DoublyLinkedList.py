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
    
    def get(self, index):
        if index < 0 or index >= self.length:
            print("index out of bound")
            return None
        if index < self.length / 2:
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
        else:
            tmp = self.tail
            for _ in range(self.length - 1, index, -1):
                tmp = tmp.prev
        return tmp
    
    def set_value(self, index, value):
        tmp = self.get(index)
        if tmp:
            tmp.value = value
            return True
        return None
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node
        
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        before = self.get(index - 1)
        after = before. next
        before.next = after.next
        after.next.prev = before
        self.length -= 1
        return after
                
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
        
dll = DoublyLinkedList(0)
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.printList()
print("pop-off: ",dll.remove(4).value)
dll.printList()