In Python

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