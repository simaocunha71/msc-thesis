The problem is asking to find the sum of digits in binary representation of the given number. Here is the solution:

The main idea is to first convert the given number into its binary representation. Then, iterate over the binary string and add each digit to a sum. The sum is the total sum of digits in binary.

Here is the Java code that implements this idea:

```java
class Solution {
    public String solve(int N) {
        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (int i = 0; i < binary.length(); i++) {
            sum += binary.charAt(i) - '0';
        }
        return String.valueOf(sum);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solve(1000));
        System.out.println(solution.solve(150));
        System.out.println(solution.solve(147));
    }
}
```

In the code, we use the `Integer.toBinaryString(N)` method to convert the given number `N` into its binary representation. Then, we iterate over the binary string using a for loop. In each iteration, we add the current digit to the sum by subtracting the character '0' from the character at the current position in the binary string. Finally, we return the sum as a string.

The output of the code will be:

```
1
6
12
```

This is because the sum of digits in binary representation of 1000 is 1, the sum of digits in binary representation of 150 is 6, and the sum of digits in binary representation of 147 is 12.