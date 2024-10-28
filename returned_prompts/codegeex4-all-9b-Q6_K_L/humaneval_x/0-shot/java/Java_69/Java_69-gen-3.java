```java
import java.util.*;
import java.lang.*;

class Solution {
    public int search(List<Integer> lst) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : lst) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        int max = -1;
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            if (entry.getValue() >= entry.getKey() && entry.getKey() > max) {
                max = entry.getKey();
            }
        }
        return max;
    }
}
```