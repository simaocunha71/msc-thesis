Here is the Java code for the problem:

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

Explanation:

*   We start by checking if the input list is empty. If it is, we return an empty list.
*   We then initialize `minEvenValue` to `Integer.MAX_VALUE` and `minIndex` to `-1`. These variables will store the smallest even value and its index, respectively.
*   We iterate through the list using a for loop. For each element, we check if it's even (`arr.get(i) % 2 == 0`) and if it's smaller than the current `minEvenValue`. If both conditions are true, we update `minEvenValue` and `minIndex`.
*   After the loop, we check if `minEvenValue` is still `Integer.MAX_VALUE`. If it is, it means that there were no even values in the list, so we return an empty list.
*   Otherwise, we add `minEvenValue` and `minIndex` to the result list and return it. The list contains the smallest even value and its index.

This solution has a time complexity of O(n), where n is the size of the input list, because we iterate through the list once. The space complexity is O(1), as we only use a constant amount of space to store the result and the variables.