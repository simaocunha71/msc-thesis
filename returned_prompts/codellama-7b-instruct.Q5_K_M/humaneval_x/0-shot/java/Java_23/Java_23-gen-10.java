import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return length of given string
    >>> strlen("")
    0
    >>> strlen("abc")
    3
     */
    public int strlen(String string) {
        return string.length();
    }

    /**
    Return string with first letter capitalized
    >>> capitalize("hello")
    "Hello"
    >>> capitalize("goodbye")
    "Goodbye"
     */
    public String capitalize(String string) {
        return string.substring(0, 1).toUpperCase() + string.substring(1);
    }

    /**
    Return true if given string is palindrome
    >>> is_palindrome("racecar")
    true
    >>> is_palindrome("hello")
    false
     */
    public boolean is_palindrome(String string) {
        return string.equals(string.toLowerCase().substring(0, string.length() / 2).toUpperCase() + string.toLowerCase().substring(string.length() / 2, string.length()));
    }

    /**
    Return true if given string is palindrome, otherwise return false
    >>> is_palindrome("racecar")
    true
    >>> is_palindrome("hello")
    false
     */
    public boolean is_palindrome(String string) {
        return string.equals(string.toLowerCase().substring(0, string.length() / 2).toUpperCase() + string.toLowerCase().substring(string.length() / 2, string.length()));
    }

    /**
    Return true if given string is palindrome, otherwise return false
    >>> is_palindrome("racecar")
    true
    >>> is_palindrome("hello")
    false
     */
    public boolean is_palindrome(String string) {
        return string.equals(string.toLowerCase().substring(0, string.length() / 2).toUpperCase() + string.toLowerCase().substring(string.length() / 2, string.length()));
    }

    /**
    Return true if given