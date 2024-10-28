```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object splitWords(String txt) {
        // if the text contains a whitespace, split on it
        if (txt.contains(" ")) {
            return txt.split(" ");
        }
        // if the text contains a comma, split on it
        else if (txt.contains(",")) {
            return txt.split(",");
        }
        // if the text contains no whitespace or comma, return the number of lowercase letters with odd order in the alphabet
        else {
            int count = 0;
            for (char c : txt.toCharArray()) {
                if (Character.isLowerCase(c) && (c - 'a') % 2 == 1) {
                    count++;
                }
            }
            return count;
        }
    }
}
```