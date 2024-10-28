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
        // Check if x and y are valid
        if (x < 1 || y < 1) {
            return -1;
        }

        // Check if there's an even number in the range
        for (int i = y; i >= x; i--) {
            if (i % 2 == 0) {
                return i;
            }
        }

        // If no even number is found, return -1
        return -1;
    }
}
```

Explanation:
This function first checks if the input numbers `x` and `y` are valid (greater than 0). If not, it returns -1.

Then it iterates over the range from `y` to `x` (inclusive) and checks each number to see if it's even (i.e., `i % 2 == 0`). If it finds an even number, it returns that number.

If it doesn't find any even number in the range, it returns -1.

Note that the function uses a for loop to iterate over the range, starting from `y` and going down to `x`. This is because we want to find the largest even number in the range, and we can do that by starting from the highest possible value and working our way down. The loop decrements `i` by 1 each iteration, so we can use `i >= x` as the loop condition.

The function also uses the modulo operator (`%`) to check if a number is even. The remainder of an even number divided by 2 is 0, so if `i % 2 == 0`, then `i` is even. If `i % 2 != 0`, then `i` is odd. This is a simple and efficient way to check if a number is even.