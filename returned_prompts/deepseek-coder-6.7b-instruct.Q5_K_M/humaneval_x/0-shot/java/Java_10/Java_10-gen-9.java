    if (isPalindrome(string))
        return string;

    for (int i = 0; i < string.length(); i++) {
        if (isPalindrome(string.substring(0, string.length() - i))) {
            StringBuilder sb = new StringBuilder(string.substring(0, string.length() - i));
            return string + sb.reverse().toString();
        }
    }

    return null;
}
}


A: Here is the code:
import java.util.*;
import java.lang.*;

class Solution {

    /**
     * Test if given string is a palindrome
     */
    public boolean isPalindrome(String string) {
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i) != string.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    /**
     * Find the shortest palindrome that begins with a supplied string.
     * Algorithm idea is simple:
     * - Find the longest postfix of supplied string that is a palindrome.
     * - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
     * >>> makePalindrome("")
     * ""
     * >>> makePalindrome("cat")
     * "catac"
     * >>> makePalindrome("cata")
     * "catac"
     */
    public String makePalindrome(String string) {

        if (isPalindrome(string))
            return string;

        for (int i = 0; i < string.length(); i++) {
            if (isPalindrome(string.substring(0, string.length() - i))) {
                StringBuilder sb = new StringBuilder(string.substring(0, string.length() - i));
                return string + sb.reverse().toString();
            }
        }

        return null;
    }
}

This