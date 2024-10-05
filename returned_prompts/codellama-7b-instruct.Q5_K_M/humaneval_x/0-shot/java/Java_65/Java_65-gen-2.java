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

        String str = String.valueOf(x);
        int len = str.length();

        if (shift > len) {
            return new StringBuilder(str).reverse().toString();
        }

        StringBuilder sb = new StringBuilder(len);
        for (int i = 0; i < len - shift; i++) {
            sb.append(str.charAt(shift + i));
        }

        for (int i = 0; i < shift; i++) {
            sb.append(str.charAt(i));
        }

        return sb.toString();
    }
}
