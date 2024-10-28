```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    returns encoded string by shifting every character by 5 in the alphabet.
     */
    public String encodeShift(String s) {
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append((char) ('a' + ((ch + 5 - 'a') % 26)));
        }
        return sb.toString();
    }

    /**
    takes as input string encoded with encodeShift function. Returns decoded string.
     */
    public String decodeShift(String s) {
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append((char) ('a' + ((ch - 5 + 26 - 'a') % 26)));
        }
        return sb.toString();
    }
}
```

The `decodeShift` function is almost the same as the `encodeShift` function, but with a small change. Instead of adding 5 to the character's ASCII value, we subtract 5. We also add 26 before taking the modulo to ensure that the result is a positive number. This is necessary because the modulo operation with a negative number can result in a negative number, which is not a valid character.