Here is a simple Java program that solves the problem:

```java
import java.util.*;

class Solution {
    public int digits(int n) {
        int product = 1;
        boolean isAllEven = true;
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
                isAllEven = false;
            }
            n /= 10;
        }
        return isAllEven ? 0 : product;
    }
}
```

In this program, we iterate over all the digits of the number and multiply the odd digits together. If all digits are even, we return 0; otherwise, we return the product of odd digits.