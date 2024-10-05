Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int minSubArraySum(List<Integer> nums) {
        int currentSum = 0;
        int minSum = Integer.MAX_VALUE;

        for (int num : nums) {
            currentSum = Math.min(currentSum + num, num);
            minSum = Math.min(minSum, currentSum);
        }

        return minSum == Integer.MAX_VALUE ? 0 : minSum;
    }
}
```
The algorithm works as follows:

1. Initialize `currentSum` and `minSum` to 0. `currentSum` will keep track of the sum of the current subarray, and `minSum` will keep track of the minimum sum of any subarray found so far.
2. Iterate over each number `num` in the array.
3. Update `currentSum` to be the minimum of `currentSum + num` and `num`. This is because if `currentSum + num` is greater than `num`, it means that adding `num` to the current subarray would increase the sum, so we should start a new subarray with `num` as the only element.
4. Update `minSum` to be the minimum of `minSum` and `currentSum`. This is because the current subarray might have a smaller sum than any subarray found so far.
5. Return `minSum`. If no subarray was found (i.e., `minSum` is still `Integer.MAX_VALUE`), return 0.