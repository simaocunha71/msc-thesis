import java.util.*;
import java.lang.*;

class Solution {
    /**
    The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
     */
    public int fibfib(int n) {
        int a = 0;
        int b = 0;
        int c = 1;
        while (n > 0) {
            if (n % 2 == 0) {
                a = b;
                b = c;
                c = a + b + c;
                n -= 2;
            } else {
                a = b;
                b = c;
                c = a + b + c;
                n--;
            }
        }
        return c;
    }
}