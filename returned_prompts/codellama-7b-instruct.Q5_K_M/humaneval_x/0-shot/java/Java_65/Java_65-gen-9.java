import java.util.*;
import java.lang.*;

class Solution {
    /**
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circularShift(12, 1)
    "21"
    >>> circularShift(12, 2)
    "12"
     */
    public String circularShift(int x, int shift) {
        if (shift > 0)
            return String.valueOf(x).substring(shift) + String.valueOf(x).substring(0, shift);
        else
            return String.valueOf(x).substring(shift) + String.valueOf(x).substring(0, shift);
    }
}
