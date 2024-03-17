Array - 1,2,3,4,5,6,7
BIG OMEGA - 1 give BEST case
BIG THETA - 4 give the AVERAGE case
BIG O     - 7 give the WORST case
---------------------------------------
BIG O is ALWAYS WORSE case
---------------------------------------
O(1) - Constant Time

public static void addItems(int n) {
    return n + n;
}
---------------------------------------
O(log n) - Divide and Conquer - Halving the array(Log base to the 2) e.g Binary Search
           Need Sorted Array

public static void printItems(int n) {
    for (int i = 0; i < n; i++){
        System.out.println(n)
    }
}
---------------------------------------
O(n) - Linear Time

public static void printItems(int n) {
    for (int i = 0; i < n; i++){
        System.out.println(n)
    }
}
---------------------------------------
O(n log n) - sorting algorithms such as quick sort
---------------------------------------
O(n^2) - Quadratic Time

public static void printItems(int n) {
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            System.out.println(i + " " + j);
        }
    }
}



---------------------------------------
|    Different terms for Inputs       |
---------------------------------------
O(a + b)

public static void printItems(int a, int b) {
    for (int i = 0; i < a; i++){
         System.out.println(a);
    }
    for (int j = 0; j < b; j++){
        System.out.println(b);
    }
}
---------------------------------------
O(ab)

public static void printItems(int a, int b) {
    for (int i = 0; i < a; i++){
        for (int j = 0; j < b; j++){
            System.out.println(i + " " + j);
        }
    }
}
---------------------------------------
Drop Constant

O(2n) -> O(n)
---------------------------------------
Drop non-dominant

 O(n^2) + O(n) -> O(n^2)
---------------------------------------
---------------------------------------
|              ArrayList              |
---------------------------------------
.add/.remove tail -> O(1)
.add/.remove head -> O(n)
.add/.remove mid  -> O(n) WORST CASE of O(1/2n)

.findByValue -> O(n)
.findByIndex -> O(1)
