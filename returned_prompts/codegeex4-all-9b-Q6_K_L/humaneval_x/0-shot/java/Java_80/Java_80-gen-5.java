```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isHappy(String s) {
        // check if the string is null or empty
        if (s == null || s.isEmpty()) {
            return false;
        }

        // check if the string length is less than 3
        if (s.length() < 3) {
            return false;
        }

        // check if every 3 consecutive letters are distinct
        for (int i = 0; i < s.length() - 2; i++) {
            if (s.charAt(i) == s.charAt(i + 1) || s.charAt(i) == s.charAt(i + 2) || s.charAt(i + 1) == s.charAt(i + 2)) {
                return false;
            }
        }

        return true;
    }
}
```