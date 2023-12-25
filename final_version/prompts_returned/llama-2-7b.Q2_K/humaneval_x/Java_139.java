import java.util.*;
import java.lang.*;

class Solution {
    /**
    The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> specialFactorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
     */
    public long specialFactorial(int n) {
        if (n == 0) {
            return 1;
        }
        for (long i = 2; ; ) {
            n--;
            if (i < n) {
                break;
            } else if (i > n) {
                continue;
            }
            int num = (int)Math.round(n * .5);
            long res = specialFactorial(num);
            long nextFactorial = factorial(n + 1);
            if (!Long.valueOf(res).equals(nextFactorial)) {
                break;
            }
        }
        return res;
    }
}
