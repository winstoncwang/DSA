class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.top is None:
            print("Empty stack")
            return None
        tmp = self.top
        self.top = tmp.next
        tmp.next = None
        self.length -= 1
        return True
        
    def printStack(self):
        tmp = self.top
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next
        print("Top: ", self.top.value)
        return
    
    
stack = Stack(1)
stack.push(2)
stack.pop()
stack.pop()
stack.pop()
stack.push(1)
stack.push(2)
print("-----------")
stack.printStack()