```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        if (txt.length() == 0) {
            return false;
        }
        char lastChar = txt.charAt(txt.length() - 1);
        return Character.isLetter(lastChar) && !txt.matches(".*\\w" + lastChar + "\\b");
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.checkIfLastCharIsALetter("apple pie")); // false
        System.out.println(solution.checkIfLastCharIsALetter("apple pi e")); // true
        System.out.println(solution.checkIfLastCharIsALetter("apple pi e ")); // false
        System.out.println(solution.checkIfLastCharIsALetter("")); // false
    }
}
```

This solution checks if the last character is a letter and not part of a word by using a regular expression. The `Character.isLetter` method checks if the last character is a letter, and the regular expression `.*\\w` + lastChar + "\\b" checks if the last character is part of a word. The `\\b` in the regular expression represents a word boundary, so the last character is not part of a word if it is followed by a word boundary.