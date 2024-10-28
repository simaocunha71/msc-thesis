You can use a simple dynamic programming approach to solve this problem. The idea is to keep track of the minimum sum of subarray ending at each position and update the result accordingly.

Here is the Java code for the solution:

```java
import java.util.*;

class Solution {
    public int minSubArraySum(List<Integer> nums) {
        int minSum = Integer.MAX_VALUE;
        int currentSum = 0;

        for (int num : nums) {
            currentSum += num;
            minSum = Math.min(minSum, currentSum);
            if (currentSum > 0) {
                currentSum = 0;
            }
        }

        return minSum;
    }
}
```

In this code, we initialize `minSum` to `Integer.MAX_VALUE` and `currentSum` to 0. We then iterate through the list of numbers. For each number, we add it to `currentSum` and update `minSum` if `currentSum` is less than `minSum`. If `currentSum` becomes positive, we reset it to 0. Finally, we return `minSum`.

This solution has a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the input list. It works by maintaining a running sum of the numbers and updating the minimum sum whenever the running sum becomes negative. This approach ensures that we consider all possible non-empty subarrays and find the minimum sum of any of them.