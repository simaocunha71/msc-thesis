```java
import java.util.*;
import java.lang.*;

class Solution {
    public int minSubArraySum(List<Integer> nums) {
        if (nums.size() == 0) return 0;
        int minSum = Integer.MAX_VALUE;
        int currentSum = 0;
        for (int num : nums) {
            currentSum += num;
            minSum = Math.min(minSum, currentSum);
            if (currentSum > 0) currentSum = 0;
        }
        return minSum;
    }
}
```

Explanation:
The solution uses the Kadane's algorithm, which is an efficient method to find the maximum sum subarray in a given array of integers.

- If the array is empty, return 0.
- Initialize `minSum` with the maximum possible integer value and `currentSum` with 0.
- Iterate through the array, adding each element to `currentSum`.
- Update `minSum` with the minimum value between `minSum` and `currentSum`.
- If `currentSum` becomes greater than 0, reset it to 0 because a negative sum will only decrease the sum of the subarray.
- Return `minSum` as the minimum sum of any non-empty sub-array.

This solution has a time complexity of O(n), where n is the length of the array, and a space complexity of O(1).