Here is the solution:

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
        if (isPalindrome(string)) {
            return string;
        }
        for (int i = string.length() - 1; i >= 0; i--) {
            String prefix = string.substring(0, i + 1);
            String postfix = string.substring(i + 1);
            String revPostfix = new StringBuilder(postfix).reverse().toString();
            if (isPalindrome(prefix + revPostfix)) {
                return prefix + revPostfix;
            }
        }
        return string; // Should not reach here
    }
}
```

This code defines a class `Solution` with two methods: `isPalindrome` and `makePalindrome`. The `isPalindrome` method checks whether a given string is a palindrome. The `makePalindrome` method finds the shortest palindrome that begins with a supplied string. It does this by finding the longest postfix of the supplied string that is a palindrome, and then appending the reverse of the string prefix that comes before the palindromic suffix. If the supplied string is already a palindrome, the method returns the string as is. If not, the method iterates over the string from the end to the beginning, and for each prefix, it checks whether the prefix and the reverse of the remaining part of the string form a palindrome. If it finds such a prefix, it returns the prefix and the reverse of the remaining part. If it does not find such a prefix, it returns the original string. This approach ensures that the returned palindrome is the shortest possible one.