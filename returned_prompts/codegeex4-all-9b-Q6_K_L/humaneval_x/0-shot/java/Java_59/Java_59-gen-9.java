import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largestPrimeFactor(13195)
    29
    >>> largestPrimeFactor(2048)
    2
     */
    public int largestPrimeFactor(int n) {
        // Find the largest prime factor of n
        int maxPrime = -1;
        while (n % 2 == 0) {
            maxPrime = 2;
            n >>= 1;
        }
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                maxPrime = i;
                n = n / i;
            }
        }
        if (n > 2) {
            maxPrime = n;
        }
        return maxPrime;
    }
}