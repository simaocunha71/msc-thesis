```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (c.indexOf(ch) == -1) {
                sb.append(ch);
            }
        }
        String result = sb.toString();
        boolean isPalindrome = result.equals(new StringBuilder(result).reverse().toString());
        return Arrays.asList(result, isPalindrome);
    }
}
```