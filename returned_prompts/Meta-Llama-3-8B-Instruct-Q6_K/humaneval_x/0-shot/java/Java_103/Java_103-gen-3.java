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
        int rounded = (int) Math.round(avg);
        String binary = Integer.toBinaryString(rounded);
        return binary;
    }
}
```
Explanation:
The problem asks to compute the average of the integers from n to m (inclusive), round it to the nearest integer, and then convert it to binary. If n is greater than m, return -1.

Here is the Java solution:

1. First, we check if n is greater than m. If true, we return -1.
2. We calculate the sum of the integers from n to m using a for loop.
3. We calculate the average by dividing the sum by the range of integers (m - n + 1).
4. We round the average to the nearest integer using Math.round.
5. We convert the rounded integer to binary using Integer.toBinaryString.
6. We return the binary string as the result.

For example, if we call `roundedAvg(1, 5)`, the function will calculate the sum of the integers from 1 to 5 (1 + 2 + 3 + 4 + 5 = 15), calculate the average (15 / 5 = 3), round it to the nearest integer (3), and convert it to binary ("11"). If we call `roundedAvg(7, 5)`, the function will return -1 because 7 is greater than 5.