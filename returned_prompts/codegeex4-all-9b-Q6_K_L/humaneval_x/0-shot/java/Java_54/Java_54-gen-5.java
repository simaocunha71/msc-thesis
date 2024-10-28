```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean sameChars(String s0, String s1) {
        char[] s0Chars = s0.toCharArray();
        char[] s1Chars = s1.toCharArray();
        Arrays.sort(s0Chars);
        Arrays.sort(s1Chars);
        return Arrays.equals(s0Chars, s1Chars);
    }
}
```