```java
import java.util.*;
import java.lang.*;

class Solution {
    public int largestPrimeFactor(int n) {
        // Start from the smallest prime number, 2
        int largestPrime = 2;
        while (n % 2 == 0) {
            n /= 2;
        }
        // Check for odd factors up to the square root of n
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largestPrime = i;
                n /= i;
            }
        }
        // If n is a prime number greater than 2
        if (n > 2) {
            largestPrime = n;
        }
        return largestPrime;
    }
}
```

The above Java code calculates the largest prime factor of a given number `n`. It first checks if `n` is divisible by 2 and removes all factors of 2. Then it checks for odd factors from 3 to the square root of `n`. If `n` is still greater than 2 after this process, it means that `n` itself is a prime number and is the largest prime factor.