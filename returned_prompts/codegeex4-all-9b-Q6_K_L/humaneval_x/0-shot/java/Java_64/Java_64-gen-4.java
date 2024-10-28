```java
import java.util.*;
import java.lang.*;

class Solution {
    public int vowelsCount(String s) {
        s = s.toLowerCase();
        int count = 0;
        for (char c : s.toCharArray()) {
            if ("aeiou".indexOf(c) != -1) {
                count++;
            }
        }
        if (s.length() > 0 && s.charAt(s.length() - 1) == 'y') {
            count++;
        }
        return count;
    }
}
```