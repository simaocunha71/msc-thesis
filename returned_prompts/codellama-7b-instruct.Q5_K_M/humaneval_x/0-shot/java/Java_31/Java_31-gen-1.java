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
        if (n < 2) {
            return false;
        }
        for (int i = 2; i <= (int) Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
