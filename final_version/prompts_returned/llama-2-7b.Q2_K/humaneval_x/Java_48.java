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
        if (text == null || text.length() < 2) return false;
        int m = text.length();
        for (int i=0;i<m-1;++i) {
            String t = new StringBuilder().append(text).reverse().toString();
            if (!t.equals(text)) {
                return false;
            }
        }
        return true;
    }
}