Here is a solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean primeLength(String string) {
        int length = string.length();
        if (length < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(length); i++) {
            if (length % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```
In this solution, we first get the length of the input string. If the length is less than 2 (since 1 is not a prime number), we return false. Otherwise, we check if the length is divisible by any number up to the square root of the length. If it is, we return false. If we've checked all possible divisors and haven't found any, we return true.