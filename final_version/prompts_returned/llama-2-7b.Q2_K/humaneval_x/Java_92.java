import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.

    Examples
    anyInt(5, 2, 7) -> true

    anyInt(3, 2, 2) -> false

    anyInt(3, -2, 1) -> true

    anyInt(3.6, -2.2, 2) -> false
     */
    public boolean anyInt(Object x, Object y, Object z) {
        if (!(x instanceof Integer && y instanceof Integer && z instanceof Integer)) {
            return false;
        } else{
            int a = (int)(x);
            int b = (int)(y);
            int c = (int)(z);
            
            if(a == 0)
                return false;
            else if((b + c) == ((long)Math.abs((-a)))) { //(b+c) is the sum of a and b and also z minus the abs value of a.
                return true;
            }
            return false;
        }
    }
}