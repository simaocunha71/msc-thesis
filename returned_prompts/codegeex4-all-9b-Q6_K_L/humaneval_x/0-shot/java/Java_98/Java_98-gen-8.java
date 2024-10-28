```java
import java.util.*;
import java.lang.*;

class Solution {
    public int countUpper(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i += 2) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c) && isVowel(c)) {
                count++;
            }
        }
        return count;
    }

    private boolean isVowel(char c) {
        return c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}
```