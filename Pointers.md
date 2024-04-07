[Python]

Primitives are hold the actual copy of the value
x = 42
y = x
// y store the actual value 42 not a reference. Changing "x" does not change y.
x = 33
// x = 33
// y = 42

Object reference are references/pointers to that memory address
a = [1,2,3]
b = a
b.append(4)

//b = [1,2,3,4]
//a = [1,2,3,4]
Both point to the same memory address.

[JAVA]
---------------------
|   Not a pointer   |
---------------------
int num1 = 11;
int num2 = num1;

num1 = 22

//num1 = 22
//num2 = 11

---------------------
|  A valid Pointer  |
---------------------
// In Java, there is no pointers but references which are pointers with safety features.
HashMap<String, Integer> map1 = new HashMap<>();
HashMap<String, Integer> map2 = new HashMap<>();

map1.put("value",11);
map2= map1

System.out.println(map1):
System.out.println(map2);

//map2 points to map1 not {"value":11}




[Understanding pointers more - Python by reference]
- given: tmp = self.root
tmp.next = new_node is really saying self.root.next = new_node
tmp = new_node is really saying tmp changed from self.root to new_node?

Yes, exactly. Let's break it down:

tmp = self.root: This assigns tmp to reference the same object as self.root. So, any changes made to tmp will also affect self.root.

tmp.next = new_node: This statement modifies the next attribute of the object referenced by tmp (which is the same as self.root). So, it's equivalent to saying self.root.next = new_node.

tmp = new_node: This statement reassigns tmp to reference a different object (new_node). So, tmp no longer points to the same object as self.root. Any changes made to tmp after this assignment will not affect self.root.

Therefore, in summary:

tmp.next = new_node affects self.root.next.
tmp = new_node changes tmp to reference a different object, but it doesn't directly affect self.root.

- so does that mean if self.root has property value. tmp = self.root. tmp.value = 54 will change self.root.value to 54?

Yes, that's correct. If tmp is assigned to self.root, then modifying properties of tmp will affect the corresponding properties of self.root.

For example:

python
Copy code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

self.root = Node(10)
tmp = self.root
tmp.value = 54
print(self.root.value)  # Output: 54
In this example, changing tmp.value to 54 also changes self.root.value to 54, because tmp is referencing the same object as self.root. Any changes made to tmp (or any attributes of the object tmp references) will directly affect self.root.