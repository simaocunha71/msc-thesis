```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> generateIntegers(int a, int b) {
        int min = Math.min(a, b);
        int max = Math.max(a, b);
        List<Integer> result = new ArrayList<>();
        for (int i = min; i <= max; i++) {
            if (i % 2 == 0) {
                result.add(i);
            }
        }
        return result;
    }
}
```