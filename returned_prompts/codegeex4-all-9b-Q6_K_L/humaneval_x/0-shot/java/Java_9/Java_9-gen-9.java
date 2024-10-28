```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> maxs = new ArrayList<>();
        int max = Integer.MIN_VALUE;

        for (int n : numbers) {
            max = Math.max(max, n);
            maxs.add(max);
        }

        return maxs;
    }
}
```