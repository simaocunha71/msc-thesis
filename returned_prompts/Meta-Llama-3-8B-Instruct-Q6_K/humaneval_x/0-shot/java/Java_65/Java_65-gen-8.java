Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public String circularShift(int x, int shift) {
        String str = String.valueOf(x);
        int len = str.length();
        if (shift > len) {
            shift = shift % len;
        }
        return str.substring(len - shift) + str.substring(0, len - shift);
    }
}
```

This solution first converts the integer x to a string. It then calculates the length of the string. If the shift is greater than the length of the string, it takes the remainder of the shift when divided by the length of the string.

Finally, it uses the substring method to extract two parts of the string: the last `shift` characters and the remaining characters. It then concatenates these two parts in the correct order to form the result. If the shift is greater than the length of the string, this will effectively reverse the string. If the shift is 0, this will return the original string. If the shift is 1, this will return the string with the first character moved to the end. And so on.