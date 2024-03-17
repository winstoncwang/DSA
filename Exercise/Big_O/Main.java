package Exercise.Big_O;

// The method is defined as public and static, meaning it can be accessed from any class without needing to create an instance of the class it belongs to.
// The method returns void, meaning it will not return any value.
// The method accepts a single parameter, an integer n. The method will use this value to determine the number of items to be printed.
public class Main {
//The method should include a for loop. The loop should start with a counter i initialized at 0, continue as long as i is less than n, and increment i by 1 with each iteration.
//Inside the loop, the method should print the current value of i to the console followed by a new line.

    // O(n)
    public static void printItems(int n){
        for(int i = 0; i < n; i++){
            System.out.println(i);
        }
    }

    // DO NOT CHANGE THE MAIN METHOD BELOW
    public static void main(String[] args) {
        printItems(10);
    }
}
