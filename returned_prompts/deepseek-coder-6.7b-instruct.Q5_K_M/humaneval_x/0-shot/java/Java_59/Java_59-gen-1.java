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

        int largest = -1;

        // Divide n by 2 until n becomes odd
        while(n % 2 == 0) {
            largest = 2;
            n >>= 1;
        }

        // n must be odd at this point. So we can skip
        // one element (Note i = i +2)
        for(int i = 3; i <= Math.sqrt(n); i += 2) {
            while(n % i == 0) {
                largest = i;
                n = n / i;
            }
        }

        // this condition is to handle the case when
        // n is a prime number greater than 2
        if(n > 2)
            largest = n;

        return largest;
    }
}

Note: The largest prime factor