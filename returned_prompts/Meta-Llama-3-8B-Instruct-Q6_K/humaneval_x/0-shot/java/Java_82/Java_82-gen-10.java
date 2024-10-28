```java
import java.util.*;

class Solution {
    public boolean primeLength(String string) {
        int length = string.length();
        if (length <= 1) {
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

Explanation:
The function `primeLength` takes a string as input and returns `true` if the length of the string is a prime number, and `false` otherwise.

We first check if the length of the string is less than or equal to 1. In this case, we return `false` because the length of a string with 0 or 1 characters is not a prime number.

Next, we use a loop to check if the length of the string is divisible by any integer from 2 to the square root of the length. If it is, we return `false` because the length is not a prime number.

If the function hasn't returned `false` by the end of the loop, we return `true` because the length of the string is a prime number.

The examples you provided demonstrate the correct behavior of the function. For example, the length of the string "Hello" is 5, which is a prime number, so the function returns `true`. Similarly, the length of the string "abcdcba" is 7, which is also a prime number, so the function returns `true`. On the other hand, the length of the string "orange" is 6, which is not a prime number, so the function returns `false`.