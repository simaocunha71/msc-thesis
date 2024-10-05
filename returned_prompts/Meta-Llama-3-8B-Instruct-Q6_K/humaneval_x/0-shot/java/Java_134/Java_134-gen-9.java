Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        if (txt.length() == 0) {
            return false;
        }
        char lastChar = txt.charAt(txt.length() - 1);
        if (!Character.isLetter(lastChar)) {
            return false;
        }
        if (txt.lastIndexOf(" ") != txt.length() - 1) {
            return false;
        }
        return true;
    }
}
```
Here's an explanation of the solution:

1. First, we check if the input string is empty. If it is, we return `false`.
2. We then get the last character of the string using `txt.charAt(txt.length() - 1)`.
3. We check if the last character is a letter using `Character.isLetter(lastChar)`. If it's not, we return `false`.
4. We then check if the last character is part of a word by checking if the last space in the string is immediately before the last character. If it's not, we return `false`.
5. If all the above conditions are met, we return `true`.

This solution works by checking the last character of the string and ensuring that it's a letter and not part of a word. It uses the `Character.isLetter()` method to check if the character is a letter, and the `lastIndexOf()` method to find the last space in the string. If the last space is not immediately before the last character, it means that the last character is part of a word, and we return `false`. Otherwise, we return `true`.