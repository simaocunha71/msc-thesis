```java
import java.util.*;
import java.lang.*;

class Solution {
    public String encode(String message) {
        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    if ("AEIOU".indexOf(c) != -1) {
                        result.append((char) (c + 2));
                    } else {
                        result.append(Character.toLowerCase(c));
                    }
                } else {
                    if ("aeiou".indexOf(c) != -1) {
                        result.append((char) (c + 2));
                    } else {
                        result.append(Character.toUpperCase(c));
                    }
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}
```