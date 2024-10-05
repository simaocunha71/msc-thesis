```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        String[] groups = paren_string.split(" ");
        List<Integer> result = new ArrayList<>();
        for (String group : groups) {
            int depth = 0;
            int maxDepth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    depth += 1;
                    maxDepth = Math.max(depth, maxDepth);
                } else if (c == ')') {
                    depth -= 1;
                }
            }
            result.add(maxDepth);
        }
        return result;
    }
}
```