# Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.
# Given this LinkedList:
# 1 -> 2 -> 3 -> 4
# If k=1 then return the first node from the end (the last node) which contains the value of 4.
# If k=2 then return the second node from the end which contains the value of 3, etc.
# If the index is out of bounds, the program should return None.
# The find_kth_from_end function should follow these requirements:
# The function should utilize two pointers, slow and fast, initialized to the head of the linked list.
# The fast pointer should move k nodes ahead in the list.
# If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
# The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
# The function should return the slow pointer, which will be at the k-th position from the end of the list.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def pop(self):
        tmp = pre = self.head
        while tmp.next is not None:
            pre = tmp
            tmp = tmp.next
        self.tail = pre
        pre.next = None
        if self.head == self.tail:
            self.head = self.tail = None
        return True
        
  
  
        
def find_kth_from_end(list, index):
    fast = list.head
    slow = list.head
    for _ in range(index):
        if fast is not None: #this cannot be fast.next, since increment will check until the 4th loop which will return 1 loop early, result k = 5 equal None(wrong).
            fast = fast.next #check fast will also eliminate edge case where the list is empty.
        else:
            return None
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

#   1 - 2 - 3 - 4 - 5


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

