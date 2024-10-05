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

        // 1. convert int to String
        String s = String.valueOf(x);
        // 2. reverse String
        String sReverse = new StringBuilder(s).reverse().toString();
        // 3. shift digits
        StringBuilder sb = new StringBuilder();
        for (int i = shift; i < sReverse.length(); i++) {
            sb.append(sReverse.charAt(i));
        }
        for (int i = 0; i < shift; i++) {
            sb.append(sReverse.charAt(i));
        }
        // 4. reverse again
        String result = new StringBuilder(sb.toString()).reverse().toString();
        // 5. return String
        return result;
    }
}
