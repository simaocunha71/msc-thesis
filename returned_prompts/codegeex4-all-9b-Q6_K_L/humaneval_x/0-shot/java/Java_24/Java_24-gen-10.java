Here is the Java code that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int largestDivisor(int n) {
        for (int i = n - 1; i > 0; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return -1; // if no divisor is found
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.largestDivisor(15)); // 5
    }
}
```

This code works by starting from n - 1 and decreasing the number until it finds a number that divides n evenly. If no divisor is found, it returns -1.