```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            if (!c.contains(String.valueOf(s.charAt(i)))) {
                result += s.charAt(i);
            }
        }
        return Arrays.asList(result, result.equals(new StringBuilder(result).reverse().toString()));
    }
}
```