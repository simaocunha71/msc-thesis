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
        int roundedAvg = (int) Math.round(avg);
        String binary = Integer.toBinaryString(roundedAvg);
        return binary;
    }
}
```


Explanation:
The problem requires you to calculate the average of the integers from n through m (inclusive), round it to the nearest integer, convert that to binary, and return the binary string.

Here's the step-by-step solution:

1. Check if n is greater than m. If true, return -1.
2. Calculate the sum of the integers from n to m using a for loop.
3. Calculate the average by dividing the sum by the number of integers (m - n + 1).
4. Round the average to the nearest integer using Math.round.
5. Convert the rounded average to a binary string using Integer.toBinaryString.
6. Return the binary string.

Note that the problem doesn't specify the type of the returned object, so we return an Object. In this case, the returned object is a String. If the problem required a different type, we would need to modify the return statement accordingly. For example, if the problem required an integer, we would return the parsed integer instead of the binary string.