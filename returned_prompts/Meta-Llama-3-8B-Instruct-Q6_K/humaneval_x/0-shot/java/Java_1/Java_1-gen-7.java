Here is a Java solution to the problem:

```java
import java.util.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int count = 0;
        
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                count++;
                sb.append(c);
            } else if (c == ')') {
                count--;
                sb.append(c);
                if (count == 0) {
                    result.add(sb.toString());
                    sb = new StringBuilder();
                }
            } else {
                sb.append(c);
            }
        }
        return result;
    }
}
```

This solution iterates over the input string, counting the number of open and close parentheses. When it encounters a close parenthesis and the count reaches zero, it means it has found a complete group, so it adds the group to the result list and resets the builder. The result list contains all the separate groups of nested parentheses.