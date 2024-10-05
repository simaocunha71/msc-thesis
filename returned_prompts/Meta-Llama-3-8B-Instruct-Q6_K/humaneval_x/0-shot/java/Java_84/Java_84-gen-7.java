The problem is asking to return the total sum of the digits in binary representation of a given positive integer N.

Here is the Java solution for the problem:
```java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solve(1000)); // prints "1"
        System.out.println(solution.solve(150)); // prints "110"
        System.out.println(solution.solve(147)); // prints "1100"
    }
}
```
The `solve` method in the `Solution` class is used to solve the problem. It first converts the integer `N` to a binary string using `Integer.toBinaryString(N)`. Then, it calculates the sum of the digits in the binary string by iterating over the characters in the string and adding their numeric values. Finally, it converts the sum back to a binary string using `Integer.toBinaryString(sum)` and returns the result.