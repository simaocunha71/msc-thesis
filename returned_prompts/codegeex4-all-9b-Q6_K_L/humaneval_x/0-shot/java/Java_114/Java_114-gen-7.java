```java
import java.util.*;
import java.lang.*;

class Solution {
    public int minSubArraySum(List<Integer> nums) {
        if (nums == null || nums.size() == 0) {
            return 0;
        }

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

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.minSubArraySum(Arrays.asList(2, 3, 4, 1, 2, 4))); // Output: 1
        System.out.println(solution.minSubArraySum(Arrays.asList(-1, -2, -3))); // Output: -6
    }
}
```