Here is the solution in Java:
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

*   We define a function `primeLength` that takes a string as input and returns a boolean value.
*   We calculate the length of the input string using the `length()` method.
*   We check if the length is less than or equal to 1, in which case we return `false` because prime numbers are greater than 1.
*   We then use a for loop to check if the length is divisible by any number between 2 and the square root of the length.
*   If the length is divisible by any number, we return `false` because it's not a prime number.
*   If the length is not divisible by any number, we return `true` because it's a prime number.

Note: The `Math.sqrt()` method is used to calculate the square root of the length, which is used as the upper bound for the for loop. This is because a larger factor of the length would be a multiple of a smaller factor that has already been checked.