Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for (int num : numbers) {
            result.add(Math.max(num, max));
            max = Math.max(num, max);
        }
        return result;
    }
}
```

This solution iterates through the list of numbers, updating the maximum value found so far and adding the maximum value found at each step to the result list. The result list will contain the rolling maximum values found until each moment in the sequence. 

The time complexity of this solution is O(n), where n is the number of elements in the input list, because it iterates through the list once. The space complexity is also O(n), because it needs to store the result list. 

The unit test `rollingMax(Arrays.asList(1, 2, 3, 2, 3, 4, 2))` will return the expected result `[1, 2, 3, 3, 3, 4, 4]`.  This is because the rolling maximum values at each step are 1, 2, 3, 3, 3, 4, 4.  The maximum value found so far at each step is also 1, 2, 3, 3, 3, 4, 4.  Therefore, the result list contains the rolling maximum values found until each moment in the sequence.  This is the expected output for the given input. 

This solution is efficient and easy to understand. It uses a simple and intuitive approach to solve the problem. It is also easy to implement and test.  Therefore, it is a good solution for this problem. 