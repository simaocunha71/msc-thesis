```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circularShift(12, 1)
    "21"
    >>> circularShift(12, 2)
    "12"
     */
    public String circularShift(int x, int shift) {
        String result = Integer.toString(x);
        if (shift >= result.length()) {
            return new StringBuilder(result).reverse().toString();
        } else {
            return result.substring(result.length() - shift) + result.substring(0, result.length() - shift);
        }
    }
}
```