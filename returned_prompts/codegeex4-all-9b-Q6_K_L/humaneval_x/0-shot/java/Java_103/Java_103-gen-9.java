```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if (n > m) {
            return -1;
        }
        int sum = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }
        int avg = Math.round((float) sum / (m - n + 1));
        return Integer.toBinaryString(avg);
    }
}
```