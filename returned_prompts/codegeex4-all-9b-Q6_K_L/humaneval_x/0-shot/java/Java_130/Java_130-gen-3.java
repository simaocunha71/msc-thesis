```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> tri(int n) {
        List<Integer> result = new ArrayList<>();
        if (n < 0) return result;
        result.add(3);
        if (n == 0) return result;
        result.add(1);
        if (n == 1) return result;
        result.add(2);
        if (n == 2) return result;
        for (int i = 3; i <= n; i++) {
            int value = result.get(i - 1) + result.get(i - 2) + result.get(i - 3);
            if (i % 2 == 0) value += i / 2;
            result.add(value);
        }
        return result;
    }
}
```
