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
    Return true if string contains given char
    >>> strcontain("abc", 'a')
    True
    >>> strcontain("abc", 'c')
    True
    >>> strcontain("abc", 'z')
    False
     */
    public boolean strcontain(String string, char character) {
        return string.contains(String.valueOf(character));
    }

    /**
    Return true if string starts with given prefix
    >>> strstartswith("abc", "a")
    True
    >>> strstartswith("abc", "c")
    False
    >>> strstartswith("abc", "ab")
    True
     */
    public boolean strstartswith(String string, String prefix) {
        return string.startsWith(prefix);
    }

    /**
    Return true if string ends with given suffix
    >>> strendswith("abc", "c")
    True
    >>> strendswith("abc", "a")
    False
    >>> strendswith("abc", "bc")
    True
     */
    public boolean strendswith(String string, String suffix) {
        return string.endsWith(suffix);
    }

    /**
    Return true if string contains only given characters
    >>> stronlychars("abc", "abc")
    True
    >>> stronlychars("abc", "cba")
    False
    >>> stronlychars("abc", "abcd")
    False
     */
    public boolean stronlychars(String string, String characters) {
        String onlyChars = string.replaceAll("[^" + characters + "]", "");
        return string.equals(onlyChars);
    }

    /**
    Return true if string is palindrome
    >>> strispalindrome("racecar")
    True
    >>> strispalindrome("level")
    False
    >>> stris