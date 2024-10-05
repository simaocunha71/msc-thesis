Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        List<Integer> result = new ArrayList<>();
        if (arr.isEmpty()) {
            return result;
        }
        int minEvenValue = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < minEvenValue) {
                minEvenValue = arr.get(i);
                minIndex = i;
            }
        }
        if (minEvenValue == Integer.MAX_VALUE) {
            return result;
        }
        result.add(minEvenValue);
        result.add(minIndex);
        return result;
    }
}
```

The solution works by iterating through the array, keeping track of the smallest even value and its index. If no even values are found, the result will be an empty list. If there are multiple even values with the same smallest value, the one with the smallest index will be chosen. Finally, the result is returned as a list with two elements: the smallest even value and its index.