```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        // Use StringBuilder to efficiently remove characters from the string
        StringBuilder sb = new StringBuilder(s);
        
        // Remove all characters in c from s
        for (char ch : c.toCharArray()) {
            int index = sb.indexOf(String.valueOf(ch));
            while (index != -1) {
                sb.deleteCharAt(index);
                index = sb.indexOf(String.valueOf(ch));
            }
        }
        
        // Check if the result string is a palindrome
        String result = sb.toString();
        boolean isPalindrome = result.equals(new StringBuilder(result).reverse().toString());
        
        // Return the result string and the palindrome check
        return Arrays.asList(result, isPalindrome);
    }
}
```
