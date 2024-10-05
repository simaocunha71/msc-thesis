```java
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
        // Check if the range is valid
        if (x > y) {
            return -1;
        }
        
        // Check if x is even
        if (x % 2 == 0) {
            return x;
        }
        
        // If x is odd, increment x by 1 to make it even
        x++;
        
        // Check if x is within the range
        if (x > y) {
            return -1;
        }
        
        return x;
    }
}
```