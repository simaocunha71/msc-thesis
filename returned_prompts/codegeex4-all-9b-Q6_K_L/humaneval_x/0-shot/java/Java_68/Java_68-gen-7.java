```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        if (arr.isEmpty()) {
            return new ArrayList<>();
        }

        int minEvenValue = Integer.MAX_VALUE;
        int minEvenIndex = -1;

        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0 && value < minEvenValue) {
                minEvenValue = value;
                minEvenIndex = i;
            }
        }

        if (minEvenIndex == -1) {
            return new ArrayList<>();
        }

        return Arrays.asList(minEvenValue, minEvenIndex);
    }
}
```