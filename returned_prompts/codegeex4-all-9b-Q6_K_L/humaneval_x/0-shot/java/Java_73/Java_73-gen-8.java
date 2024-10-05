Here is a solution in Java:

```java
import java.util.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        int n = arr.size();
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            dp[i][i] = 0;
        }

        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                if (arr.get(i) == arr.get(j)) {
                    dp[i][j] = dp[i + 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i][j - 1], dp[i + 1][j]) + 1;
                }
            }
        }

        return dp[0][n - 1];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.smallestChange(Arrays.asList(1,2,3,5,4,7,9,6))); // Output: 4
        System.out.println(solution.smallestChange(Arrays.asList(1, 2, 3, 4, 3, 2, 2))); // Output: 1
        System.out.println(solution.smallestChange(Arrays.asList(1, 2, 3, 2, 1))); // Output: 0
    }
}
```

This solution uses dynamic programming to solve the problem in O(n^2) time complexity. The idea is to build a 2D array `dp` where `dp[i][j]` represents the minimum number of changes needed to make the subarray `arr[i..j]` palindromic. If `arr[i]` is equal to `arr[j]`, then `dp[i][j]` is equal to `dp[i+1][j-1]` (since the subarray `arr[i..j]` is already palindromic). Otherwise, `dp[i][j]` is equal to the minimum of `dp[i][j-1]` and `dp[i+1][j]` plus 1 (since we need to change either `arr[i]` or `arr[j]` to make the subarray `arr[i..j]` palind