    if (isPalindrome(string)) {
        return string;
    }
    int len = string.length();
    for (int i = len; i >= 0; i--) {
        if (isPalindrome(string.substring(0, i))) {
            StringBuilder sb = new StringBuilder(string.substring(0, len - i));
            return string + sb.reverse().toString();
        }
    }
    return null;
}
}


A: Your solution is correct and good, but the problem is that it checks from the end to the start, so it's not efficient. It should be better to check from the start to the end. 
Here is your solution improved:

import java.util.*;
import java.lang.*;

class Solution {
    /**
    Test if given string is a palindrome
    */
    public boolean isPalindrome(String string) {
        int i = 0;
        int j = string.length() - 1;
        while(i < j) {
            if(string.charAt(i) != string.charAt(j)) {
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
        if(isPalindrome(string)) {
            return string;
        }
        int len = string.length();
        for(int i = 0; i < len; i++) {
            if(isPalindrome(string.substring(0, len - i))) {
                StringBuilder sb = new StringBuilder(string.substring(len - i));