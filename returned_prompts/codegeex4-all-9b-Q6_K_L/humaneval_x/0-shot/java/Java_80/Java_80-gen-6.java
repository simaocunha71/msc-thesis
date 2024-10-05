Here is the Java code for the problem:

```java
import java.util.*;

class Solution {
    public boolean isHappy(String s) {
        if (s.length() < 3) {
            return false;
        }
        for (int i = 0; i < s.length() - 2; i++) {
            if (s.charAt(i) == s.charAt(i + 1) || s.charAt(i) == s.charAt(i + 2) || s.charAt(i + 1) == s.charAt(i + 2)) {
                return false;
            }
        }
        return true;
    }
}
```

This code first checks if the length of the string is less than 3. If it is, it returns false because a happy string must have at least 3 characters.

Then it loops through the string, checking each 3-letter segment to see if any characters are repeated. If it finds any repeated characters, it returns false. If it doesn't find any repeated characters, it returns true.