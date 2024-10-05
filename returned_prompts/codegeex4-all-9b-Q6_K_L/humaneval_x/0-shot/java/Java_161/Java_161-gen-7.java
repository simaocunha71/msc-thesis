```java
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(String s) {
        String result = "";
        boolean hasLetter = false;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                result += Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c);
                hasLetter = true;
            } else {
                result += c;
            }
        }
        if (!hasLetter) {
            result = new StringBuilder(s).reverse().toString();
        }
        return result;
    }
}
```