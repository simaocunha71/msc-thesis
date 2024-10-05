```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (!c.contains(String.valueOf(s.charAt(i)))) {
                sb.append(s.charAt(i));
            }
        }
        String result = sb.toString();
        boolean isPalindrome = result.equals(new StringBuilder(result).reverse().toString());
        return Arrays.asList(result, isPalindrome);
    }
}
```