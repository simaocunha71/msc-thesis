Here is a Java solution for the problem. The solution counts the numbers of n-digit positive integers that start or end with 1.

```java
public class Solution {
    public int startsOneEnds(int n) {
        int count = 0;
        if (n == 1) {
            count = 2;
        } else {
            count = 2;
            for (int i = 2; i <= n; i++) {
                count += 9 * (int) Math.pow(10, i - 2);
            }
        }
        return count;
    }
}
```
Explanation:

The solution works by calculating the number of n-digit numbers that start or end with 1.

For n = 1, there are only two such numbers: 1 and 0.

For n > 1, the solution calculates the number of n-digit numbers that start or end with 1 by considering the numbers that start with 1 and the numbers that end with 1.

The numbers that start with 1 can be calculated by taking the number of (n-1)-digit numbers (which is 9 * (10^(n-1))) and adding 1.

The numbers that end with 1 can be calculated by taking the number of (n-1)-digit numbers (which is 9 * (10^(n-1))) and adding the number of (n-1)-digit numbers that end with 9 (which is 10^(n-1)).

The total number of n-digit numbers that start or end with 1 is the sum of the numbers that start with 1 and the numbers that end with 1.