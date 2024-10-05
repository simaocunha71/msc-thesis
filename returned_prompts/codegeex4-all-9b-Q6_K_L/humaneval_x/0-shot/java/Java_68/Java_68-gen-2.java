```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        if (arr == null || arr.isEmpty()) {
            return new ArrayList<>();
        }
        int minEven = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < arr.size(); i++) {
            int val = arr.get(i);
            if (val % 2 == 0 && val < minEven) {
                minEven = val;
                minIndex = i;
            }
        }
        if (minIndex == -1) {
            return new ArrayList<>();
        }
        return Arrays.asList(minEven, minIndex);
    }
}
```