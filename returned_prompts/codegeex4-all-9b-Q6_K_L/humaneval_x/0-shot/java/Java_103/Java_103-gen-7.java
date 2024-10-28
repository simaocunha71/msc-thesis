```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if (n > m) {
            return -1;
        }
        double avg = 0;
        for (int i = n; i <= m; i++) {
            avg += i;
        }
        avg /= (m - n + 1);
        avg = Math.round(avg);
        return Integer.toBinaryString((int) avg);
    }
}
```