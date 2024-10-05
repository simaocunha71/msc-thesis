Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> result = new ArrayList<>();
        int max = numbers.get(0);
        result.add(max);
        for (int i = 1; i < numbers.size(); i++) {
            max = Math.max(max, numbers.get(i));
            result.add(max);
        }
        return result;
    }
}
```

In this solution, we initialize a list `result` to store the rolling maximum elements and a variable `max` to store the maximum element found until the current moment. We start by adding the first element of the input list to the `result` list. Then, we iterate over the rest of the list. For each element, we update the `max` variable to be the maximum of the current `max` and the current element. Finally, we add the updated `max` to the `result` list. At the end of the iteration, the `result` list will contain the rolling maximum elements. 

This solution has a time complexity of O(n), where n is the size of the input list. This is because we make a single pass over the input list. The space complexity is O(n) as well, as we store the result in a list of size n. 