Here is the solution to the problem:

```java
import java.util.*;

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
        // Reverse the string
        String reversed = new StringBuilder(string).reverse().toString();

        // Find the longest postfix of the string that is a palindrome
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i) != string.charAt(j)) {
                break;
            }
            i++;
            j--;
        }
        String palindromeSuffix = string.substring(i);

        // Return the original string plus the reverse of the remaining part
        return string + reversed.substring(palindromeSuffix.length());
    }
}
```

This solution first reverses the input string to create a reversed version. Then it finds the longest postfix of the original string that is a palindrome. This is done by iterating through the string from both ends, comparing characters, and stopping when a mismatch is found. The palindrome suffix is the part of the string from the mismatched character to the end.

Finally, the solution returns the original string plus the reverse of the remaining part of the reversed string. This ensures that the resulting string is the shortest palindrome that begins with the original string.