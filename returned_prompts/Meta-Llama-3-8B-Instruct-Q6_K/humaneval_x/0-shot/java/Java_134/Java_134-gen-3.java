Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        // Check if the string is empty
        if (txt.isEmpty()) {
            return false;
        }

        // Check if the last character is an alphabetical character
        char lastChar = txt.charAt(txt.length() - 1);
        if (!Character.isLetter(lastChar)) {
            return false;
        }

        // Check if the last character is part of a word
        if (txt.charAt(txt.length() - 1) == ' ' || txt.charAt(txt.length() - 1) == '\n' || txt.charAt(txt.length() - 1) == '\t') {
            return false;
        }

        return true;
    }
}
```

The function `checkIfLastCharIsALetter` takes a string `txt` as input and returns `true` if the last character of the string is an alphabetical character and is not part of a word, and `false` otherwise.

The function first checks if the string is empty. If it is, it returns `false`.

Then, it checks if the last character of the string is an alphabetical character using the `Character.isLetter` method.

If the last character is not an alphabetical character, the function returns `false`.

If the last character is an alphabetical character, the function checks if it is part of a word by checking if it is a space, newline, or tab character. If it is, the function returns `false`.

If the last character is an alphabetical character and is not part of a word, the function returns `true`. Otherwise, it returns `false`.