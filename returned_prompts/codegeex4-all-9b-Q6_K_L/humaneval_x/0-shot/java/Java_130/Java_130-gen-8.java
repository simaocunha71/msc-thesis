```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> tri(int n) {
        List<Integer> res = new ArrayList<>();
        if (n == 0) return res;
        res.add(3);
        if (n == 1) return res;
        res.add(1);
        if (n == 2) return res;
        res.add(2);
        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                res.add(1 + i / 2);
            } else {
                res.add(res.get(i - 1) + res.get(i - 2) + res.get(i - 3));
            }
        }
        return res;
    }
}
```
