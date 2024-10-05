import java.util.*;
import java.lang.*;

class Solution {
    /**
    Test if given string is a palindrome
     */
    public boolean isPalindrome(String string) {
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i)!= string.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    /**
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> makePalindrome("")
    ""
    >>> makePalindrome("cat")
    "catac"
    >>> makePalindrome("cata")
    "catac"
     */
    public String makePalindrome(String string) {
        // Find the longest postfix of supplied string that is a palindrome
        int i = string.length();
        while (i > 0) {
            if (isPalindrome(string.substring(i))) {
                break;
            }
            i--;
        }
        String suffix = string.substring(i);
        String prefix = string.substring(0, i);
        String reversedPrefix = new StringBuilder(prefix).reverse().toString();
        return suffix + reversedPrefix;
    }
}