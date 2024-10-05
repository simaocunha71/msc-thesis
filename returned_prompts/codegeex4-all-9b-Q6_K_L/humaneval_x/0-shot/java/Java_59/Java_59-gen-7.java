```java
import java.util.*;
import java.lang.*;

class Solution {
    public int largestPrimeFactor(int n) {
        // Initialize the maximum prime factor
        int maxPrime = -1;

        // Divide n by 2 until n is odd
        while (n % 2 == 0) {
            maxPrime = 2;
            n /= 2;
        }

        // n must be odd at this point, thus a skip of 2 (i = i + 2) can be used
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            // While i divides n, update n and maxPrime
            while (n % i == 0) {
                maxPrime = i;
                n /= i;
            }
        }

        // This condition is to handle the case when n is a prime number greater than 2
        if (n > 2) {
            maxPrime = n;
        }

        return maxPrime;
    }
}
```