```java
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(String s) {
        char[] chars = s.toCharArray();
        boolean hasLetter = false;
        for (char c : chars) {
            if (Character.isLetter(c)) {
                hasLetter = true;
                break;
            }
        }
        if (!hasLetter) {
            return new StringBuilder(s).reverse().toString();
        }
        for (int i = 0; i < chars.length; i++) {
            if (Character.isLetter(chars[i])) {
                chars[i] = Character.isLowerCase(chars[i]) ? Character.toUpperCase(chars[i]) : Character.toLowerCase(chars[i]);
            }
        }
        return new String(chars);
    }
}
```