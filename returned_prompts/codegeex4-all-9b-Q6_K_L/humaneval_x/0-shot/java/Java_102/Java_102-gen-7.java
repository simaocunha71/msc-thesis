Here is the Java code to solve the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int chooseNum(int x, int y) {
        // If x is odd, add 1 to make it even
        if (x % 2 != 0) {
            x++;
        }
        
        // If y is odd, subtract 1 to make it even
        if (y % 2 != 0) {
            y--;
        }
        
        // If x is greater than y, return -1
        if (x > y) {
            return -1;
        }
        
        // Return the biggest even number in the range [x, y]
        return y;
    }
}
```

This code works by first checking if x and y are odd or even. If they are odd, it adds or subtracts 1 to make them even. Then, it checks if x is greater than y. If it is, it returns -1. Finally, it returns y, which is the biggest even number in the range [x, y].