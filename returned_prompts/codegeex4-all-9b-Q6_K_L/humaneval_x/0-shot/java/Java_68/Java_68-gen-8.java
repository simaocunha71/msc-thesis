```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        List<Integer> result = new ArrayList<>();
        if (arr == null || arr.isEmpty()) {
            return result;
        }
        int minEven = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < arr.size(); i++) {
            int num = arr.get(i);
            if (num % 2 == 0 && num < minEven) {
                minEven = num;
                minIndex = i;
            }
        }
        if (minIndex != -1) {
            result.add(minEven);
            result.add(minIndex);
        }
        return result;
    }
}
```