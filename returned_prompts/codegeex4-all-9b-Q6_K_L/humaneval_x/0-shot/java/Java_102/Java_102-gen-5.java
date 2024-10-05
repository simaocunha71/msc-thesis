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
        // Check if x and y are positive
        if (x <= 0 || y <= 0) {
            return -1;
        }
        
        // If x is odd, increment it by 1 to make it even
        if (x % 2 != 0) {
            x++;
        }
        
        // If x is greater than y, there's no even number in the range
        if (x > y) {
            return -1;
        }
        
        // Return the biggest even number in the range
        return x;
    }
}
```