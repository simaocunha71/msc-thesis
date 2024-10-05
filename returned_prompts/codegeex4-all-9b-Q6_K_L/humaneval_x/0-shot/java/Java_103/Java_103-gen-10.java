```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if (n > m) {
            return -1;
        }

        double sum = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }

        double avg = sum / (m - n + 1);
        int roundedAvg = (int) Math.round(avg);

        return Integer.toBinaryString(roundedAvg);
    }
}
```