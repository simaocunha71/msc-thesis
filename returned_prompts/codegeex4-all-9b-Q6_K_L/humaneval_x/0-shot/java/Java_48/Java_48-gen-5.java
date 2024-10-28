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
        if(text == null || text.length() == 0) {
            return true;
        }
        int start = 0;
        int end = text.length() - 1;
        while(start < end) {
            if(text.charAt(start) != text.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
```