Here is a Java solution that implements the described functionality:

```java
import java.util.*;

class Solution {
    public Object roundedAvg(int n, int m) {
        if (n > m) {
            return -1;
        }

        int sum = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }

        double avg = (double) sum / (m - n + 1);
        int roundedAvg = (int) Math.round(avg);

        return Integer.toBinaryString(roundedAvg);
    }
}
```

This solution first checks if `n` is greater than `m`. If it is, the function returns `-1`. Otherwise, it calculates the sum of the integers from `n` to `m` and computes the average. The average is then rounded to the nearest integer using `Math.round()`. Finally, the binary representation of the rounded average is returned using `Integer.toBinaryString()`.