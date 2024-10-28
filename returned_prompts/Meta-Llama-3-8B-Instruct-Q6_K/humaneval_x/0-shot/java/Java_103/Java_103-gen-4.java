Here is the Java code that solves the problem:

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

This code first checks if n is greater than m. If it is, the function returns -1. Then it calculates the sum of the integers from n to m (inclusive) using a for loop. It calculates the average by dividing the sum by the number of integers (m - n + 1). It rounds the average to the nearest integer using Math.round(). Finally, it converts the rounded average to binary using Integer.toBinaryString() and returns the result.