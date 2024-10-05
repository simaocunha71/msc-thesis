Here is the solution to the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split("\\s+");
        for (String group : groups) {
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

This solution works by iterating over each group of parentheses in the input string. For each group, it keeps track of the current depth of nesting and the maximum depth reached so far. Whenever it encounters an opening parenthesis, it increments the current depth and updates the maximum depth if necessary. Whenever it encounters a closing parenthesis, it decrements the current depth. Finally, it adds the maximum depth to the result list. The solution uses the `split` method to split the input string into groups, and the `toCharArray` method to iterate over the characters in each group. The `Math.max` method is used to update the maximum depth. The solution returns a list of integers, where each integer represents the maximum depth of nesting for the corresponding group of parentheses. 