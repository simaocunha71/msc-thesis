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
        if (n <= 1) return 1;
        int p = 3, t = 2;
        
        while (true) {
            if (t * t == n) break;
            
            // check for prime numbers
            if ((p + 1 > Integer.MAX_VALUE / t || Math.pow(n, (p+1)/t) < p*t) && n % p == 0) {
                return p;
            } else {
                if (Math.pow(n, t/2) <= n && n % t == 0){
                    return t;
                }
                p++;
            }
        }
        
        return -1;
    }
}