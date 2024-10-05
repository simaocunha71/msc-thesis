import java.util.*;
import java.lang.*;

class Solution {
    /**
    A simple program which should return the value of x if n is
    a prime number and should return the value of y otherwise.

    Examples:
    for xOrY(7, 34, 12) == 34
    for xOrY(15, 8, 5) == 5
     */
    public int xOrY(int n, int x, int y) {
        if (isPrime(n)) {
            return x;
        } else {
            return y;
        }
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}