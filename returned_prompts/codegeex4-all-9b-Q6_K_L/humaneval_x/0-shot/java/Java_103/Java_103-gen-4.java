```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if (n > m) {
            return -1;
        }
        int sum = 0;
        int count = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
            count++;
        }
        double avg = (double) sum / count;
        int roundedAvg = (int) Math.round(avg);
        return Integer.toBinaryString(roundedAvg);
    }
}
```
