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

        if (n <= 1) {
            return n;
        }
        int n1 = 0;
        int n2 = 1;
        for (int i = 2; i <= n; i++) {
            n1 = n2;
            n2 = n1 + n2;
        }
        return n2;
    }
}
