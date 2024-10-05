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
        // Check if both x and y are even
        if ((x % 2 == 0) && (y % 2 == 0)) {
            // Return the biggest even number
            return y;
        } else if ((x % 2 != 0) && (y % 2 == 0)) {
            // Check if there's an even number in the range
            for (int i = x; i <= y; i++) {
                if (i % 2 == 0) {
                    return i;
                }
            }
        } else {
            // No even numbers in the range
            return -1;
        }
    }
}
```
Explanation:
The function first checks if both x and y are even. If they are, it returns the largest even number, which is y.

If x is odd and y is even, the function checks if there's an even number in the range [x, y] by iterating from x to y and checking if each number is even. If it finds an even number, it returns that number.

If neither x nor y is even, the function returns -1, indicating that there's no even number in the range.