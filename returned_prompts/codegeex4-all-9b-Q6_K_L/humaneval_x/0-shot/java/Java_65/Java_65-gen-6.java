You can use the built-in methods of the String class to solve this problem. Here is the Java code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String circularShift(int x, int shift) {
        String s = Integer.toString(x);
        if (shift > s.length()) {
            return new StringBuilder(s).reverse().toString();
        }
        return s.substring(s.length() - shift) + s.substring(0, s.length() - shift);
    }
}
```

The code first converts the integer to a string. Then, if the shift is greater than the length of the string, it reverses the string and returns it. Otherwise, it uses the `substring` method of the `String` class to extract the last `shift` digits and the first `s.length() - shift` digits, and then concatenates them together to get the result.