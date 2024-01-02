import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return a greatest common divisor of two integers a and b
    >>> greatestCommonDivisor(3, 5)
    1
    >>> greatestCommonDivisor(25, 15)
    5
     */
    public int greatestCommonDivisor(int a, int b) {
        if (b == 0) return a;
        else if (a % b < 0) return greatestCommonDivisor(b, a-b);
        else if (a%b > 0 ) return greatestCommonDivisor(a-b, b);
        else return a;
    }
}