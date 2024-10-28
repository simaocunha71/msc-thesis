```java
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(String s) {
        boolean hasLetters = false;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                hasLetters = true;
                break;
            }
        }
        if (!hasLetters) {
            StringBuilder sb = new StringBuilder(s);
            return sb.reverse().toString();
        }
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    sb.append(Character.toLowerCase(c));
                } else {
                    sb.append(Character.toUpperCase(c));
                }
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
```