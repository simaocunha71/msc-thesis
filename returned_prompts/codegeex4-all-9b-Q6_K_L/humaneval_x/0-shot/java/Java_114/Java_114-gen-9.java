```java
import java.util.*;
import java.lang.*;

class Solution {
    public int minSubArraySum(List<Integer> nums) {
        int n = nums.size();
        int[] dp = new int[n];
        dp[0] = nums.get(0);
        int minSum = dp[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.min(nums.get(i), dp[i - 1] + nums.get(i));
            minSum = Math.min(minSum, dp[i]);
        }
        return minSum;
    }
}
```