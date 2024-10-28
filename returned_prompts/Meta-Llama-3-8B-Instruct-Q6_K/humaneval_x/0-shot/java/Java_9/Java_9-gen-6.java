```java
import java.util.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> maxList = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for (int num : numbers) {
            maxList.add(Math.max(num, max));
            max = Math.max(num, max);
        }
        return maxList;
    }
}
```

Explanation:
The problem is asking to find the maximum element in a given list of integers until that moment in the sequence. This is known as the rolling maximum problem.

The solution is simple, we iterate through the list of numbers and for each number, we calculate the maximum of the current number and the maximum found so far. We then add this maximum to our result list.

We use the `Math.max()` function to find the maximum of two numbers. This function returns the maximum of its two arguments.

In the end, we return the list of rolling maximum elements. This list will contain the maximum element found up to each point in the sequence.