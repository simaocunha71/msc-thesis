Here is a Java solution to parse the nested parentheses:

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        for (String group : paren_string.split("\\s+")) {
            int maxDepth = 0;
            int currentDepth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    currentDepth++;
                    maxDepth = Math.max(maxDepth, currentDepth);
                } else if (c == ')') {
                    currentDepth--;
                }
            }
            result.add(maxDepth);
        }
        return result;
    }
}
```

In this solution, we split the input string into groups by spaces. Then for each group, we initialize `maxDepth` and `currentDepth` to 0. We iterate over the characters in the group. If we encounter a `(`, we increment `currentDepth` and update `maxDepth` if necessary. If we encounter a `)`, we decrement `currentDepth`. Finally, we add `maxDepth` to the result list.

For example, if the input is `"(()()) ((())) () ((())()())"`, the output will be `[2, 3, 1, 3]`. 

The time complexity of this solution is O(n), where n is the total number of characters in the input string. The space complexity is O(n), where n is the number of groups in the input string. 