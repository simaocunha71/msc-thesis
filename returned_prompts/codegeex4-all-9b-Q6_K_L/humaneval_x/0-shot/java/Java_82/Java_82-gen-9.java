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
This solution checks if the length of the string is a prime number. It first checks if the length is less than 2, in which case it returns false because 2 is the smallest prime number. Then it checks if the length is divisible by any number from 2 to the square root of the length. If it is divisible by any of these numbers, it returns false because it is not a prime number. Otherwise, it returns true.