```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rollingMax(Arrays.asList(1, 2, 3, 2, 3, 4, 2))
    [1, 2, 3, 3, 3, 4, 4]
     */
    public List<Integer> rollingMax(List<Integer> numbers) {
        if (numbers == null || numbers.isEmpty()) {
            return new ArrayList<>();
        }
        
        List<Integer> result = new ArrayList<>();
        int max = numbers.get(0);
        result.add(max);
        
        for (int i = 1; i < numbers.size(); i++) {
            int current = numbers.get(i);
            if (current > max) {
                max = current;
            }
            result.add(max);
        }
        
        return result;
    }
}
```

Explanation:
- The method `rollingMax` takes a list of integers as input and returns a new list containing the rolling maximum of the input list.
- If the input list is null or empty, an empty list is returned.
- The first element of the input list is initialized as the maximum value.
- A new list `result` is created to store the rolling maximum values.
- The first element of `result` is set to the maximum value.
- The method then iterates through the remaining elements of the input list.
- For each element, the method checks if it is greater than the current maximum value.
- If it is, the maximum value is updated to the current element.
- The current maximum value is then added to the `result` list.
- Finally, the `result` list is returned.