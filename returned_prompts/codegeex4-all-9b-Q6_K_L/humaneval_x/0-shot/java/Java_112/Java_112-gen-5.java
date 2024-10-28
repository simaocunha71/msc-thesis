```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Object> reverseDelete(String s, String c) {
        List<Object> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (c.indexOf(ch) == -1) {
                sb.append(ch);
            }
        }
        String newS = sb.toString();
        result.add(newS);
        result.add(newS.equals(new StringBuilder(newS).reverse().toString()));
        return result;
    }
}
```