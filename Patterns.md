[LinkedList]
- FindMiddleNode - Use slow/fast(2 steps) pointer. Check fast and fast.next is not None to prevent fast.next erroring out None. Since fast can be none.

- HasLoop - Use slow/fast(2 steps) pointer, loop until slow == fast. Which uses the hare and tortoise algorithm

- FindKthNodeFromEnd - set slow/fast at head, set fast to increment (kth steps) if None, we have a kth node larger than the list. If not None, distance between slow and fast will be k step away. move both pointer by 1 increment until fast is None. return slow.

- Reverse LL - using three pointers which prevents the breaking of the connection between tmp and after

[DoublyLinkedList]
- Reverse through current, current.next and current.prev swap using tmp pointer. Then move the current node to the previous(which is now the next node) and traverse through the list.

[Stack&Queue]
- Stack can use both list and linked list. Queue uses linked list. Stack only uses one pointer(top). Queue uses 2 pointer(first and last), and enqueue(add) will be added to the last pointer(from the tail, since append is O(1), but popping is O(n))