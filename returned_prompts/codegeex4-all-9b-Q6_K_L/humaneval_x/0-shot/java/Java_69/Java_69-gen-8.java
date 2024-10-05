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
            int num = entry.getKey();
            int freq = entry.getValue();
            if (freq >= num && num > max) {
                max = num;
            }
        }
        return max;
    }
}
```