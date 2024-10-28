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
        long result = 1;
        for (int i = n; i >= 1; i--) {
            long factorial = 1;
            for (int j = i; j >= 1; j--) {
                factorial *= j;
            }
            result *= factorial;
        }
        return result;
    }
}