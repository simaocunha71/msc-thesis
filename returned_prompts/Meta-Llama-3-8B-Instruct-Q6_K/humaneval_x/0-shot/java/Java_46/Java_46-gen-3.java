```java
import java.util.*;

public class Solution {
    public int fib4(int n) {
        if (n <= 1) {
            return 0;
        }
        if (n == 2) {
            return 2;
        }
        int[] fib4 = new int[n + 1];
        fib4[1] = 0;
        fib4[2] = 2;
        for (int i = 3; i <= n; i++) {
            fib4[i] = fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4];
        }
        return fib4[n];
    }
}
```

Explanation:
This solution uses dynamic programming to efficiently compute the n-th element of the fib4 number sequence. It first checks the base cases where n is less than or equal to 1, or n is 2. For n greater than 2, it initializes an array `fib4` of size `n+1` to store the fib4 numbers. It then iterates from 3 to n, computing each fib4 number as the sum of the previous four numbers. Finally, it returns the nth element of the array, which is the n-th fib4 number. This solution has a time complexity of O(n) and a space complexity of O(n).