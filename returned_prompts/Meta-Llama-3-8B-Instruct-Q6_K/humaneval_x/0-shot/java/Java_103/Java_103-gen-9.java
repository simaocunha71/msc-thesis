Here is the solution in Java:
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
        String binary = Integer.toBinaryString(roundedAvg);
        return binary;
    }
}
```
Explanation:
1. We first check if `n` is greater than `m`. If it is, we return -1 as per the problem statement.
2. We calculate the sum of all integers from `n` to `m` (inclusive) using a for loop.
3. We calculate the average of the sum by dividing it by the number of integers (i.e., `m - n + 1`).
4. We round the average to the nearest integer using `Math.round()`.
5. We convert the rounded average to binary using `Integer.toBinaryString()`.
6. We return the binary representation of the rounded average as a string.

Note that we use `double` to store the average to ensure accurate calculations, and `Math.round()` to round the average to the nearest integer. We also use `Integer.toBinaryString()` to convert the rounded average to binary. Finally, we return the binary representation as a string.