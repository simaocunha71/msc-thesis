import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum(Arrays.asList(2, 3, 4, 1, 2, 4)) == 1
    minSubArraySum(Arrays.asList(-1, -2, -3)) == -6
     */
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