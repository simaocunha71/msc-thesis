```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean willItFly(List<Integer> q, int w) {
        if (q.size() % 2 != 0) {
            return false;
        }

        int sum = 0;
        for (int i = 0; i < q.size() / 2; i++) {
            if (q.get(i) != q.get(q.size() - i - 1)) {
                return false;
            }
            sum += q.get(i);
        }

        return sum <= w;
    }
}
```