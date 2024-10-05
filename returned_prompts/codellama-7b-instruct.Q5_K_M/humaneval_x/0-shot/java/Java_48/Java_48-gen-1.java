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
        // write your code here
        return text.equals(new StringBuilder(text).reverse().toString());
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isPalindrome(""));
        System.out.println(s.isPalindrome("aba"));
        System.out.println(s.isPalindrome("aaaaa"));
        System.out.println(s.isPalindrome("zbcd"));
    }
}
