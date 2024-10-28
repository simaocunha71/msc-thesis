```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> generateIntegers(int a, int b) {
        List<Integer> result = new ArrayList<>();
        for (int i = Math.min(a, b); i <= Math.max(a, b); i++) {
            if (i % 2 == 0) {
                result.add(i);
            }
        }
        return result;
    }
}
```