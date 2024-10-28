The question is asking to find the minimum sum of any non-empty sub-array of a given array of integers. Here is the solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int minSubArraySum(List<Integer> nums) {
        int minSum = Integer.MAX_VALUE;
        int currentSum = 0;

        for (int i = 0; i < nums.size(); i++) {
            currentSum += nums.get(i);

            if (currentSum < minSum) {
                minSum = currentSum;
            }

            if (currentSum > 0) {
                currentSum = 0;
            }
        }

        return minSum;
    }
}
```

The solution works by iterating through the array and keeping track of the current sum of the sub-array. If the current sum is less than the minimum sum, we update the minimum sum. If the current sum is greater than 0, we reset the current sum to 0.

The time complexity of this solution is O(n), where n is the length of the input array.