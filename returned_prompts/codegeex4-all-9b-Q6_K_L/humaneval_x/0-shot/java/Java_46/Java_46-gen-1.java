Here is the Java code to solve the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fib4(int n) {
        int[] dp = new int[n+1];
        dp[0] = 0;
        dp[1] = 0;
        dp[2] = 2;
        dp[3] = 0;

        for(int i = 4; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4];
        }
        return dp[n];
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.fib4(5));  // Output: 4
        System.out.println(sol.fib4(6));  // Output: 8
        System.out.println(sol.fib4(7));  // Output: 14
    }
}
```

This code uses dynamic programming to efficiently compute the n-th element of the fib4 number sequence. It initializes an array `dp` to store the computed values, then iteratively computes each value in the sequence based on the previous four values. The time complexity of this solution is O(n), which is much more efficient than the recursive solution.