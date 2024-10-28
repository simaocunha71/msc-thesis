```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    isEqualToSumEven(4) == false
    isEqualToSumEven(6) == false
    isEqualToSumEven(8) == true
     */
    public boolean isEqualToSumEven(int n) {
        // Check if the number is even
        if (n % 2 != 0) {
            return false;
        }
        // Check if the number can be written as the sum of exactly 4 positive even numbers
        return n >= 8;
    }
}
```