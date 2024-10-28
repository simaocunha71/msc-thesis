Here is the Java code for the problem. It first checks if the input string is a palindrome. If it is, it simply returns the string. If it is not, it finds the longest palindromic suffix of the string, and appends the reverse of the remaining prefix to the end of the string.

```java
import java.util.*;

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
        // if the string is already a palindrome, just return it
        if (isPalindrome(string)) {
            return string;
        }
        // find the longest palindromic suffix of the string
        int len = string.length();
        for (int i = len; i > 0; i--) {
            String suffix = string.substring(len - i);
            if (isPalindrome(suffix)) {
                // if the prefix is not empty, append the reverse of the prefix to the end of the suffix
                if (i < len) {
                    return suffix + new StringBuilder(string.substring(0, len - i)).reverse().toString();
                } else {
                    return suffix;
                }
            }
        }
        // if no palindromic suffix is found, return the original string
        return string;
    }
}
```

This code works by first checking if the input string is a palindrome. If it is, it simply returns the string. If it is not, it finds the longest palindromic suffix of the string by iterating from the end of the string backwards. It checks each suffix to see if it is a palindrome, and if it is, it appends the reverse of the remaining prefix to the end of the suffix