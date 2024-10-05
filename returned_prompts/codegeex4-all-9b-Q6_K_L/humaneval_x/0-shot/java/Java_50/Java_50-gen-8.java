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
The `decodeShift` function is almost the same as the `encodeShift` function, but it shifts the characters by -5 instead of +5. The `% 26` ensures that the result is always in the range of 0 to 25, which corresponds to the letters of the alphabet.