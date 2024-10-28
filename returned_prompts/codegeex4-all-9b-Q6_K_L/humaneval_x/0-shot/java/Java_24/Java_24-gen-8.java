Here is a Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int largestDivisor(int n) {
        for (int i = n / 2; i > 0; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return -1; // If no divisor is found, return -1
    }
}
```

This code works by looping from n / 2 down to 1 and checking if n is divisible by each number. When it finds a number that divides n evenly (i.e., n % i == 0), it returns that number. If no number is found that divides n evenly, it returns -1.