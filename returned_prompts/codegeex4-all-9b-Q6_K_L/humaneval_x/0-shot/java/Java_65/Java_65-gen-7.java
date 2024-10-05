Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public String circularShift(int x, int shift) {
        String str = String.valueOf(x);
        int len = str.length();
        if (shift > len) {
            return new StringBuilder(str).reverse().toString();
        }
        String left = str.substring(len - shift);
        String right = str.substring(0, len - shift);
        return left + right;
    }
}
```

Explanation:
1. Convert the integer x to a string str.
2. If the shift is greater than the length of the string, reverse the string and return it.
3. Otherwise, split the string into two parts: left (the last 'shift' characters) and right (the rest of the string).
4. Concatenate the left and right parts to get the result.

This solution has a time complexity of O(n), where n is the number of digits in x.