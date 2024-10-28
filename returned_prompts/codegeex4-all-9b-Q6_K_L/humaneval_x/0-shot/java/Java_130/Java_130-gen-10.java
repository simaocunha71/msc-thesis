```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> tri(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("n must be non-negative");
        }
        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(3);
        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                result.add(result.get(i - 1) + result.get(i - 2) + result.get(i + 1));
            }
        }
        return result;
    }
}
```
