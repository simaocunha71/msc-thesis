Here is the Java code that implements the `rollingMax` function:

```java
import java.util.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        int maxSoFar = Integer.MIN_VALUE;
        for (int num : numbers) {
            result.add(Math.max(num, maxSoFar));
            maxSoFar = Math.max(num, maxSoFar);
        }
        return result;
    }
}
```

This function initializes an empty list `result` to store the rolling maximum values and an integer `maxSoFar` to keep track of the maximum value seen so far. It then iterates over the input list `numbers`, updating `result` with the maximum of the current number and `maxSoFar`, and updating `maxSoFar` with the current number. Finally, it returns the `result` list.