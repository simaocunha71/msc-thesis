import java.util.*;
import java.lang.*;

class Solution {
    /**
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> changeBase(8, 3)
    "22"
    >>> changeBase(8, 2)
    "1000"
    >>> changeBase(7, 2)
    "111"
     */
    public String changeBase(int x, int base) {
        // write your code here
        if (x == 0) {
            return "0";
        }
        StringBuffer buf = new StringBuffer();
        while (x > 0) {
            int cur = x % base;
            x /= base;
            buf.append(cur);
        }
        return buf.toString();
    }
}




