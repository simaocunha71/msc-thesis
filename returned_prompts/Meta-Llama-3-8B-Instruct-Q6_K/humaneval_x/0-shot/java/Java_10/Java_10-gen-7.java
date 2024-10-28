Here is the solution using Java:

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
        if (string == null || string.length() == 0) {
            return "";
        }
        if (isPalindrome(string)) {
            return string;
        }
        for (int i = string.length() - 1; i >= 0; i--) {
            String prefix = string.substring(0, i + 1);
            String postfix = string.substring(i + 1);
            if (isPalindrome(postfix)) {
                return prefix + new StringBuilder(postfix).reverse().toString();
            }
        }
        return "";
    }
}
```

In this solution, the `makePalindrome` function checks if the input string is a palindrome. If it is, the function returns the string itself. If not, the function finds the longest postfix of the string that is a palindrome. It then appends the reverse of the string prefix to the end of the palindromic postfix to form the shortest palindrome that begins with the supplied string. The `isPalindrome` function checks if a given string is a palindrome. It does this by comparing characters from the start and end of the string and moving towards the center. If it finds any pair of characters that do not match, it returns `false`. If it successfully checks all pairs of characters without finding a mismatch, it returns `true`. The `makePalindrome` function uses the `isPalindrome` function to find the longest postfix of the string that is a palindrome and to form the shortest palindrome that begins with the supplied string. The function returns the shortest palindrome. The `makePalindrome