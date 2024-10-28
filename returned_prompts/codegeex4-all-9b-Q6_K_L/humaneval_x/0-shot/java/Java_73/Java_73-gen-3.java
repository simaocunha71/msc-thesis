```java
import java.util.*;
import java.lang.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        int n = arr.size();
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            dp[i] = i;
        }
        for (int i = 1; i <= n / 2; i++) {
            for (int j = 0; j < n - i; j++) {
                if (arr.get(j) == arr.get(j + i)) {
                    dp[j + i + 1] = Math.min(dp[j + i + 1], dp[j]);
                } else {
                    dp[j + i + 1] = Math.min(dp[j + i + 1], dp[j] + 1);
                }
            }
        }
        return dp[n];
    }
}
```