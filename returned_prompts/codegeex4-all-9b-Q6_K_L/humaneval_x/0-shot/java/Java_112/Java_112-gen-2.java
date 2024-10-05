```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (!c.contains(String.valueOf(ch))) {
                sb.append(ch);
            }
        }
        String res = sb.toString();
        boolean isPalindrome = res.equals(new StringBuilder(res).reverse().toString());
        return Arrays.asList(res, isPalindrome);
    }
}
```