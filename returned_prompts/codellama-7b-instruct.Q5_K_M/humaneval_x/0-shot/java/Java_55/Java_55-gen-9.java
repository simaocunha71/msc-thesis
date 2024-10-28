import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
     */
    public int fib(int n) {
        // Fibonacci numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
        // Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
        // Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
        if (n < 1)
            return 0;
        if (n == 1)
            return 1;
        return fib(n-2) + fib(n-1);
    }
}