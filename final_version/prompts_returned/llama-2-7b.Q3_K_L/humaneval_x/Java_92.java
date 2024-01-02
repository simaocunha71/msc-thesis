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
        int xValue = (int)x;
        int yValue = (int)y;
        int zValue = (int)z;
        //System.out.print("X: " + x);
        
        if ((anyInt(xValue,yValue,zValue)) && (allIntegers(xValue,yValue,zValue))) {
            return true;
        } else {
            System.out.println("No Matching Sum");
            return false;
        }
    }
    
    private boolean anyInt(int x, int y, int z) {
        if (x == z && x != 0) {
            return true;
        } else {
            System.out.println("No Matching Sum");
            return false;
        }
        
    }
    
    private boolean allIntegers(int x, int y, int z) {
        if (x == Integer.MIN_VALUE && y == Integer.MAX_VALUE || x == Integer.MAX_VALUE && y == Integer.MIN_VALUE) {
            return true;
            
        } else {
            System.out.println("No Matching Sum");
            return false;
        }
    }
}