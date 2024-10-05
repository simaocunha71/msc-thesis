```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        Set<Character> set = new HashSet<>();
        for (char ch : c.toCharArray()) {
            set.add(ch);
        }
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (!set.contains(ch)) {
                sb.append(ch);
            }
        }
        String result = sb.toString();
        boolean isPalindrome = result.equals(new StringBuilder(result).reverse().toString());
        return Arrays.asList(result, isPalindrome);
    }
}
```