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

        int largest = 2;

        while (n > largest) {
            if (n % largest == 0) {
                n /= largest;
            } else {
                largest++;
            }
        }

        return largest;
    }
}