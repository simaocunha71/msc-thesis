```java
import java.util.*;
import java.lang.*;

class Solution {
    public int search(List<Integer> lst) {
        int max = -1;
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : lst) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
            if (entry.getKey() > entry.getValue()) {
                max = Math.max(max, entry.getKey());
            }
        }
        return max;
    }
}
```