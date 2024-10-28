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
        if (n <= 1) return n;
        int a = 1, b = 1;
        for (int i = 2; i <= n; i++) {
            a = b;
            b += a;
        }
        return a;
    }
}
