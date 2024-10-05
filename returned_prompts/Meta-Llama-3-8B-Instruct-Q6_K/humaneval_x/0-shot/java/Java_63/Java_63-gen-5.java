```java
import java.util.*;

public class Solution {
    public int fibfib(int n) {
        if (n <= 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }
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
```

Explanation:
The given problem is to compute the n-th element of the fibfib number sequence. The fibfib number sequence is defined as follows:
fibfib(0) == 0
fibfib(1) == 0
fibfib(2) == 1
fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

We can use dynamic programming to solve this problem efficiently. We create an array fibfib of size n+1 and initialize the first three elements as 0, 0, and 1 respectively.

Then we iterate from 3 to n and calculate the i-th element as the sum of the (i-1)th, (i-2)th, and (i-3)th elements.

Finally, we return the n-th element of the array. This solution has a time complexity of O(n) and a space complexity of O(n).

The unit tests provided in the problem statement can be used to verify the correctness of the solution. For example, `fibfib(1)` should return 0, `fibfib(5)` should return 4, and `fibfib(8)` should return 24. These tests can be used to ensure that the solution is working correctly.