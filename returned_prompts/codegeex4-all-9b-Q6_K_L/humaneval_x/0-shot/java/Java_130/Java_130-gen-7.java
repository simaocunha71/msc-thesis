```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> tri(int n) {
        List<Integer> result = new ArrayList<>(n + 1);
        result.add(1);
        result.add(3);
        for (int i = 2; i <= n; i++) {
            int value = 1 + i / 2;
            if (i % 2 != 0) {
                value += result.get(i - 1) + result.get(i - 2);
            }
            result.add(value);
        }
        return result;
    }
}
```