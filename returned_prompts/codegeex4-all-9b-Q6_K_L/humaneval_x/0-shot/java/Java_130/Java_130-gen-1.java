```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> tri(int n) {
        List<Integer> result = new ArrayList<>();
        if (n == 0) {
            result.add(3);
            return result;
        }
        result.add(3);
        result.add(1);
        result.add(3);
        for (int i = 4; i <= n + 1; i++) {
            if (i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                int val = result.get(i - 1) + result.get(i - 2) + result.get(i + 1);
                result.add(val);
            }
        }
        return result;
    }
}
```
