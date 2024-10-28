```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fibfib(int n) {
        List<Integer> fibfib = new ArrayList<>();
        fibfib.add(0);
        fibfib.add(0);
        fibfib.add(1);
        for (int i = 3; i <= n; i++) {
            fibfib.add(fibfib.get(i-1) + fibfib.get(i-2) + fibfib.get(i-3));
        }
        return fibfib.get(n);
    }
}
```