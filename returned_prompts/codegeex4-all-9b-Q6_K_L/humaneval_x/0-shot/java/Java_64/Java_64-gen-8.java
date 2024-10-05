```java
import java.util.*;
import java.lang.*;

class Solution {
    public int vowelsCount(String s) {
        int count = 0;
        String vowels = "aeiouAEIOU";
        for (int i = 0; i < s.length(); i++) {
            if (vowels.indexOf(s.charAt(i)) != -1) {
                count++;
            }
        }
        if (s.length() > 0 && s.charAt(s.length() - 1) == 'y' || s.charAt(s.length() - 1) == 'Y') {
            count++;
        }
        return count;
    }
}
```