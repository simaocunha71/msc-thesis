Here is a simple Java solution:

```java
import java.util.*;

class Solution {
    public String circularShift(int x, int shift) {
        String str = Integer.toString(x);
        if (shift >= str.length()) {
            return new StringBuilder(str).reverse().toString();
        } else {
            return str.substring(str.length() - shift) + str.substring(0, str.length() - shift);
        }
    }
}
```

This function first converts the input integer to a string. If the shift is greater than or equal to the length of the string, it returns the reversed string. Otherwise, it performs a right circular shift on the string and returns the result.