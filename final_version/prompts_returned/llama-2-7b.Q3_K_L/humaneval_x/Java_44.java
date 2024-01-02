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
        if (x == 0 || base < 1 || base > 9) throw new IllegalArgumentException();
        
        // convert it to string representation. and check its length
        String val = Integer.toString(x);
        String str = "";
        for (int i = 0; i < val.length(); i++) {
            if ((i % base == 0) && (val.charAt(i) != '0')) {
                // we should check with (i%base) here to avoid 0x, it is not a digit
                str = str + "1";
            } else if (val.charAt(i) != '0') {
                str += val.charAt(i);
            }
        }
        
        // check the length of string
        if (str.length() == 1 && str.charAt(0) == '1' ) throw new IllegalArgumentException();
        return str;
    }
}