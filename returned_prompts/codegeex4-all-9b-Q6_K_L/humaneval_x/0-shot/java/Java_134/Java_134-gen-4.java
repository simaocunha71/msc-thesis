```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        // if the string is empty, return false
        if (txt.isEmpty()) {
            return false;
        }

        // get the last character of the string
        char lastChar = txt.charAt(txt.length() - 1);

        // check if the last character is a letter and is not part of a word
        return Character.isLetter(lastChar) && !Character.isLetter(txt.charAt(txt.length() - 2));
    }
}
```