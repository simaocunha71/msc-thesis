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

We first get the length of the string using `string.length()`.

If the length is 1 or less, we immediately return `false`, since 1 and 0 are not considered prime numbers.

Then, we use a loop to check if the length is divisible by any number up to its square root. If it is, we return `false`, since the length is not a prime number.

If the length passes all these checks, we return `true`, indicating that the length is a prime number.