```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        if (arr.size() == 0) {
            return new ArrayList<>();
        }
        int min = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < min) {
                min = arr.get(i);
                minIndex = i;
            }
        }
        if (minIndex == -1) {
            return new ArrayList<>();
        }
        return Arrays.asList(min, minIndex);
    }
}
```