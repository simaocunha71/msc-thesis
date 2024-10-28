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
        String[] baseString = new String[]{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
        int quotient = x;
        String result = "";
        while(quotient > 0){
            result = baseString[quotient % base] + result;
            quotient /= base;
        }
        return result;
    }
}
