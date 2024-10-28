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

    int a = 1, b = 0, c = 0;
    while (n > 0) {
        c = a + b;
        a = b;
        b = c;
        n--;
    }
    return b;
}
}
