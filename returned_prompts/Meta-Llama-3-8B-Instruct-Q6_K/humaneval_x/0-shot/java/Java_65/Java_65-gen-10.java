Here is a Java solution using string manipulation:

```java
import java.util.*;

class Solution {
    public String circularShift(int x, int shift) {
        String str = String.valueOf(x);
        int n = str.length();
        shift = shift % n;
        if (shift == 0) {
            return str;
        }
        return str.substring(shift) + str.substring(0, shift);
    }
}
```

In this solution, we first convert the integer to a string. Then we calculate the shift percentage by taking the remainder of the shift when divided by the length of the string. If the shift is 0, we simply return the original string. Otherwise, we use the `substring` method to extract two parts of the string: the part to be shifted to the end, and the part to be kept at the beginning. We then concatenate these two parts to get the result.