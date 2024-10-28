import java.util.*;
import java.lang.*;

class Solution {
    /**
    primeFib returns n-th number that is a Fibonacci number and it's also prime.
    >>> primeFib(1)
    2
    >>> primeFib(2)
    3
    >>> primeFib(3)
    5
    >>> primeFib(4)
    13
    >>> primeFib(5)
    89
     */
    public int primeFib(int n) {
        int fib1 = 0;
        int fib2 = 1;
        int fib3 = fib1 + fib2;
        int count = 0;
        while (count < n) {
            if (isPrime(fib3)) {
                count++;
            }
            fib1 = fib2;
            fib2 = fib3;
            fib3 = fib1 + fib2;
        }
        return fib3;
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}