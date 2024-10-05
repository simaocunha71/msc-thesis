```java
import java.util.*;
import java.lang.*;

class Solution {
    public int vowelsCount(String s) {
        // convert the string to lowercase
        s = s.toLowerCase();
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                count++;
            }
            if (i == s.length() - 1 && c == 'y') {
                count++;
            }
        }
        return count;
    }
}
```