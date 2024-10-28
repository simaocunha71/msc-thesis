Here is the Java code to solve the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fibfib(int n) {
        if (n == 0 || n == 1) {
            return 0;
        } else if (n == 2) {
            return 1;
        } else {
            int[] fibfib = new int[n + 1];
            fibfib[0] = 0;
            fibfib[1] = 0;
            fibfib[2] = 1;
            for (int i = 3; i <= n; i++) {
                fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
            }
            return fibfib[n];
        }
    }
}
```

This solution uses dynamic programming to compute the n-th element of the fibfib number sequence. The fibfib array stores the computed elements of the sequence, and the for loop fills in the remaining elements. The time complexity of this solution is O(n), and the space complexity is also O(n).