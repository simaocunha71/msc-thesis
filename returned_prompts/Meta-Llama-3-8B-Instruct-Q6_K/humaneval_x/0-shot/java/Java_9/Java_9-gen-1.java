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
The code defines a `rollingMax` method that takes a list of integers as input. It initializes an empty list `result` to store the rolling maximum values and sets `max` to `Integer.MIN_VALUE` to keep track of the maximum value seen so far.

The method then iterates over the input list, and for each number, it calculates the maximum of the current number and the previous maximum `max`. This maximum value is then added to the `result` list. The `max` value is also updated to the new maximum.

Finally, the method returns the `result` list, which contains the rolling maximum values for each element in the input list.

The unit test `>>> rollingMax(Arrays.asList(1, 2, 3, 2, 3, 4, 2))` checks the output of the `rollingMax` method for the input list `[1, 2, 3, 2, 3, 4, 2]`. The expected output is `[1, 2, 3, 3, 3, 4, 4]`, which is the rolling maximum values for each element in the input list. The actual output of the `rollingMax` method matches this expected output.