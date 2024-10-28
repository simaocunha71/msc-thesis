Here is a simple Java solution for the problem:

```java
import java.util.*;

class Solution {
    public int search(List<Integer> lst) {
        Map<Integer, Integer> map = new HashMap<>();
        for (Integer num : lst) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getKey() > 0 && entry.getValue() >= entry.getKey()) {
                return entry.getKey();
            }
        }
        return -1;
    }
}
```

This solution works by first counting the frequency of each number in the list using a HashMap. Then, it iterates over the map to find the first number that is greater than 0 and has a frequency greater than or equal to the number itself. If no such number is found, it returns -1. The time complexity of this solution is O(n), where n is the size of the input list. The space complexity is also O(n), as we need to store the frequency of each number in the map.