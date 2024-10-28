```java
import java.util.*;
import java.lang.*;

class Solution {
    public int largestPrimeFactor(int n) {
        int largestPrime = -1;
        while (n % 2 == 0) {
            largestPrime = 2;
            n /= 2;
        }
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largestPrime = i;
                n /= i;
            }
        }
        if (n > 2) {
            largestPrime = n;
        }
        return largestPrime;
    }
}
```