The problem can be solved by iterating over the string `s` and removing the characters that are present in the string `c`. Then check if the resulting string is a palindrome or not.

Here is the Java code that solves the problem:

```java
import java.util.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }
        String newStr = sb.toString();
        result.add(newStr);
        result.add(isPalindrome(newStr));
        return result;
    }

    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
```

In this code, we first create a new string `newStr` by iterating over the string `s` and removing the characters that are present in the string `c`. Then we check if `newStr` is a palindrome or not using the `isPalindrome` method. The result is stored in a list and returned.

The `isPalindrome` method checks if a string is a palindrome or not by comparing characters from the start and end of the string and moving towards the center. If any pair of characters is not equal, the method returns `false`, otherwise it returns `true`.