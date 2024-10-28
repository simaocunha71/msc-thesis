```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> generateIntegers(int a, int b) {
        int start = Math.min(a, b);
        int end = Math.max(a, b);
        List<Integer> result = new ArrayList<>();
        for (int i = start; i <= end; i++) {
            if (i % 2 == 0) {
                result.add(i);
            }
        }
        return result;
    }
}
```