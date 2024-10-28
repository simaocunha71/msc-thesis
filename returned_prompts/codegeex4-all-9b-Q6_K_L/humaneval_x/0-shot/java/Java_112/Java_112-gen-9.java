```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
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