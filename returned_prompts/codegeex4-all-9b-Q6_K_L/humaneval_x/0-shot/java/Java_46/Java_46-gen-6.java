To efficiently compute the n-th element of the fib4 number sequence without using recursion, we can use dynamic programming to store the previously computed values. This way, we avoid redundant calculations and improve the performance.

Here's the updated code:

```java
import java.util.*;

class Solution {
    public int fib4(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be a non-negative integer");
        }
        
        if (n == 0 || n == 1) {
            return 0;
        }
        
        if (n == 2) {
            return 2;
        }
        
        int[] fib4 = new int[n + 1];
        fib4[0] = 0;
        fib4[1] = 0;
        fib4[2] = 2;
        
        for (int i = 3; i <= n; i++) {
            fib4[i] = fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4];
        }
        
        return fib4[n];
    }
}
```

In this code, we first handle the special cases when n is 0, 1, or 2. Then, we create an array `fib4` of size `n + 1` to store the previously computed values. We initialize the first three elements of the array based on the definition of the fib4 number sequence. Then, we use a loop to compute the remaining elements of the array. Finally, we return the n-th element of the fib4 number sequence, which is stored in `fib4[n]`.