[Tree_structure]

Full tree - Every node points to zero or two nodes.

          4
        3   23
     13   7

Perfect - Completely filled tree

          4
        3   23

Complete tree - Fill nodes from let to right. But not perfect.

          4
        3   23
    13   7  13  27
  6

A parent node without child node is a leaf.

            4
        2       5
4 is a parent node, 2,5 is a child node but also a leaf.

[BST_Binary_Search_Tree]

If the number of the node is less than the parent node, it goes to the left.
1. 47
2. 76 is more then 47 -> right
3. 52 > 47 but less than 76 -> left of child of 76

            47
        21      76
              52    82

[BST_BIG_O]
Lookup/Insert/Remove require n steps. O(log n)

            47              2^1 -1
        21      76          2^2 -1
     11    23 52    82      2^3 -1
             n              2^n (halved everytime)

[LL - BIG O]
Lookup O(n)
Insert O(1) - Insert at the end (append), if ordering is not an issue. I shouldn't since LL are usually not sorted. LL is best for quick insert.
Remove O(n)

[Comparison]
LL             vs            BST
/            INSERT          X
X            LOOKUP          /
X            REMOVE          /
