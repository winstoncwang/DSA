LinkedList
- FindMiddleNode - Use slow/fast(2 steps) pointer. Check fast and fast.next is not None to prevent fast.next erroring out None. Since fast can be none.

- HasLoop - Use slow/fast(2 steps) pointer, loop until slow == fast. Which uses the hare and tortoise algorithm

- FindKthNodeFromEnd - set slow/fast at head, set fast to increment (kth steps) if None, we have a kth node larger than the list. If not None, distance between slow and fast will be k step away. move both pointer by 1 increment until fast is None. return slow.