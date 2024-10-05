```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        if (txt.isEmpty()) {
            return false;
        }

        char lastChar = txt.charAt(txt.length() - 1);
        return Character.isLetter(lastChar) && !Character.isLetter(txt.charAt(txt.length() - 2));
    }
}
```
This solution checks if the last character of the string is an alphabetical character and is not part of a word by comparing it with the second last character. It returns true if the last character is an alphabetical character and is not part of a word, and false otherwise.