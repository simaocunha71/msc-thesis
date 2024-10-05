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
        if (minIndex != -1) {
            result.add(minEvenValue);
            result.add(minIndex);
        }
        return result;
    }
}
```
This solution iterates over the array and keeps track of the smallest even value and its index. If no even values are found, it returns an empty list. Otherwise, it returns a list containing the smallest even value and its index. The time complexity is O(n), where n is the size of the array. The space complexity is O(1), as we only use a constant amount of space to store the result.