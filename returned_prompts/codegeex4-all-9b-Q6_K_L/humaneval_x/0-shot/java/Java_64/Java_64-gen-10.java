```java
import java.util.*;
import java.lang.*;

class Solution {
    public int vowelsCount(String s) {
        if (s.length() == 0) return 0;
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y') {
                count++;
            }
        }
        if (s.endsWith("y")) count++;
        return count;
    }
}
```