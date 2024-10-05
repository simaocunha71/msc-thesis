Here is a Java solution using a stack to keep track of the maximum depth of nested parentheses:

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        String[] groups = paren_string.split(" ");
        List<Integer> result = new ArrayList<>();
        for (String group : groups) {
            int depth = 0, maxDepth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    depth++;
                    maxDepth = Math.max(depth, maxDepth);
                } else if (c == ')') {
                    depth--;
                }
            }
            result.add(maxDepth);
        }
        return result;
    }
}
```

This function splits the input string into groups and then iterates through each group. For each group, it keeps track of the current depth of nesting and the maximum depth seen so far. If it encounters an opening parenthesis, it increases the depth and updates the maximum depth. If it encounters a closing parenthesis, it decreases the depth. After processing each group, it adds the maximum depth to the result list. Finally, it returns the result list.