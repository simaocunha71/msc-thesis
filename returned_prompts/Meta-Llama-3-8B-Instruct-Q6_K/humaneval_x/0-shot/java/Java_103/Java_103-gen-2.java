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
        double roundedAvg = Math.round(avg);
        String binary = Integer.toBinaryString((int) roundedAvg);
        return binary;
    }
}
```


Explanation:

1. First, we check if `n` is greater than `m`. If it is, we return -1 as per the problem statement.
2. We calculate the sum of all integers from `n` to `m` inclusive using a for loop.
3. We calculate the average of these integers by dividing the sum by the number of integers (`m - n + 1`).
4. We round the average to the nearest integer using `Math.round()`.
5. We convert the rounded average to a binary string using `Integer.toBinaryString()`.
6. We return the binary string.

Note: The problem statement asks to round the average to the nearest integer, which is a bit ambiguous. However, based on the provided examples, it seems that the intention is to round to the nearest integer, rather than to the nearest multiple of 2. Therefore, we use `Math.round()` to round to the nearest integer. If you want to round to the nearest multiple of 2, you can use `Math.round(avg * 2) / 2` instead.