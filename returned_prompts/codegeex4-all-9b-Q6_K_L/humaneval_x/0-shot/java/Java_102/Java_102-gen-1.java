import java.util.*;
import java.lang.*;

class Solution {
    /**
    This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If
    there's no such number, then the function should return -1.
    
    For example:
    chooseNum(12, 15) = 14
    chooseNum(13, 12) = -1
     */
    public int chooseNum(int x, int y) {
        if (x > y) {
            return -1;
        }
        if (x % 2 != 0) {
            x++;
        }
        if (y % 2 != 0) {
            y--;
        }
        if (x > y) {
            return -1;
        }
        return y;
    }
}