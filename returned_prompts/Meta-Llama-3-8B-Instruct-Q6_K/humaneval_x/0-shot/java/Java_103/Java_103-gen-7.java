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
        double avg = (double) sum / (m - n + 1);
        avg = Math.round(avg);
        String binary = Integer.toBinaryString((int) avg);
        return binary;
    }
}
```


Explanation:
The problem is asking you to calculate the average of the integers from n to m (inclusive), round it to the nearest integer, and then convert it to a binary string. If n is greater than m, return -1.

The solution first checks if n is greater than m, and if so, returns -1. Otherwise, it calculates the sum of the integers from n to m using a for loop, and then calculates the average by dividing the sum by the number of integers (m - n + 1).

The average is then rounded to the nearest integer using the Math.round() function. Finally, the binary string representation of the rounded average is calculated using the Integer.toBinaryString() function, and returned as the result.

Note that the problem statement asks for the average to be rounded to the nearest integer, which means that if the average is halfway between two integers, it should be rounded up. This is achieved by using the Math.round() function, which returns the closest integer to the given double value. If the given double value is halfway between two integers, Math.round() will round up to the nearest integer.