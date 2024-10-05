```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        int max = Integer.MIN_VALUE;
        List<Integer> result = new ArrayList<>();
        for (int number : numbers) {
            max = Math.max(max, number);
            result.add(max);
        }
        return result;
    }
}
```