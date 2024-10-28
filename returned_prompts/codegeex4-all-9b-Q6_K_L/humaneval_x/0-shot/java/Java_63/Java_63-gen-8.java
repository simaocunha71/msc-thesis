Here is a solution in Java using dynamic programming:

```java
import java.util.*;

class Solution {
    public int fibfib(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n should be a non-negative integer.");
        }
        if (n == 0) {
            return 0;
        } else if (n == 1 || n == 2) {
            return 1;
        }
        int[] fibfib = new int[n+1];
        fibfib[0] = 0;
        fibfib[1] = 1;
        fibfib[2] = 1;
        for (int i = 3; i <= n; i++) {
            fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3];
        }
        return fibfib[n];
    }
}
```

This code uses an array `fibfib` to store the first `n+1` numbers of the `fibfib` sequence. It starts by initializing `fibfib[0]` and `fibfib[1]` to 0 and 1 respectively, and then calculates `fibfib[i]` for `i` from 2 to `n` using the formula `fibfib(i) = fibfib(i-1) + fibfib(i-2) + fibfib(i-3)`. Finally, it returns `fibfib[n]`. The time complexity of this solution is O(n), and the space complexity is also O(n).