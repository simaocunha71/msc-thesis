import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100.
    Example:
    isMultiplyPrime(30) == true
    30 = 2 * 3 * 5
     */
    public boolean isMultiplyPrime(int a) {
        if (a < 100) {
            return false;
        }
        for (int i = 2; i < 10; i++) {
            if (a % i == 0) {
                if (isPrime(i)) {
                    if (isPrime(a / i) && isPrime(a / (a / i))) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    private boolean isPrime(int a) {
        if (a < 100) {
            return false;
        }
        for (int i = 2; i < a / 2; i++) {
            if (a % i == 0) {
                return false;
            }
        }
        return true;
    }
}
