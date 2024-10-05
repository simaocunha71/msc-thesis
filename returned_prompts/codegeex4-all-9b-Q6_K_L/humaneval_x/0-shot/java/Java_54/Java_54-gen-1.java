```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean sameChars(String s0, String s1) {
        if (s0.length() != s1.length()) {
            return false;
        }
        int[] count = new int[256]; // ASCII character set
        for (char c : s0.toCharArray()) {
            count[c]++;
        }
        for (char c : s1.toCharArray()) {
            if (count[c] == 0) {
                return false;
            }
            count[c]--;
        }
        return true;
    }
}
```