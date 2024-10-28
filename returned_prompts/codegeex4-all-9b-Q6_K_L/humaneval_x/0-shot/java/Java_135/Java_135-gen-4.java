```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    canArrange(Arrays.asList(1,2,4,3,5)) = 3
    canArrange(Arrays.asList(1,2,3)) = -1
     */
    public int canArrange(List<Integer> arr) {
        int n = arr.size();
        int[] dp = new int[n];
        for (int i = 1; i < n; i++) {
            if (arr.get(i) >= arr.get(i - 1)) {
                dp[i] = dp[i - 1] + 1;
            } else {
                dp[i] = 1;
            }
        }
        return dp[n - 1];
    }
}
```