```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flipCase("Hello")
    "hELLO"
     */
    public String flipCase(String string) {
        StringBuilder flippedString = new StringBuilder();
        for (char c : string.toCharArray()) {
            if (Character.isLowerCase(c)) {
                flippedString.append(Character.toUpperCase(c));
            } else if (Character.isUpperCase(c)) {
                flippedString.append(Character.toLowerCase(c));
            } else {
                flippedString.append(c);
            }
        }
        return flippedString.toString();
    }
}
```