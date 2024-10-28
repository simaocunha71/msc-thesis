```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Checks if given string is a palindrome
    >>> isPalindrome("")
    true
    >>> isPalindrome("aba")
    true
    >>> isPalindrome("aaaaa")
    true
    >>> isPalindrome("zbcd")
    false
     */
    public boolean isPalindrome(String text) {
        int len = text.length();
        for (int i = 0; i < len / 2; i++) {
            if (text.charAt(i) != text.charAt(len - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}
```