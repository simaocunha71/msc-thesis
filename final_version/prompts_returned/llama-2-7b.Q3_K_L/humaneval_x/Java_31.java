import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return true if a given number is prime, and false otherwise.
    >>> isPrime(6)
    false
    >>> isPrime(101)
    true
    >>> isPrime(11)
    true
    >>> isPrime(13441)
    true
    >>> isPrime(61)
    true
    >>> isPrime(4)
    false
    >>> isPrime(1)
    false
     */
    public boolean isPrime(int n) {
        if (n <= 1) return false;
        int count = 2, maxCount = Math.sqrt(Math.abs(n));
        while (count < maxCount && n % (long)count == 0) ++count;
        
        return count >= maxCount || (count - 1 != (int)(maxCount - (long)count * .5));
    }
}