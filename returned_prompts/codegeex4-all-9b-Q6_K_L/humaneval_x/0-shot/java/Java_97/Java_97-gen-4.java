```java
import java.util.*;
import java.lang.*;

class Solution {
    public int multiply(int a, int b) {
        int lastDigitA = Math.abs(a % 10);
        int lastDigitB = Math.abs(b % 10);
        return lastDigitA * lastDigitB;
    }
}
```
The code above is a solution to the problem of multiplying the unit digits of two integers. 
It first calculates the unit digit of the first integer using the modulus operator `%` and stores it in the variable `lastDigitA`. 
It then does the same for the second integer, storing the result in the variable `lastDigitB`. 
Finally, it returns the product of `lastDigitA` and `lastDigitB`.