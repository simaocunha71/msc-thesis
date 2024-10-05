Here is the Java code that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int digits(int n) {
        int product = 1;
        boolean hasOddDigit = false;
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
                hasOddDigit = true;
            }
            n /= 10;
        }
        return hasOddDigit ? product : 0;
    }
}
```

This code works by iterating through each digit of the input number. If the digit is odd, it is multiplied to the product. If there is at least one odd digit, the product is returned. Otherwise, 0 is returned.