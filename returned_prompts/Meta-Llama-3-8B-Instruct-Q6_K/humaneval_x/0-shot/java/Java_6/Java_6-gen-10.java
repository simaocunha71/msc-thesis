Here is a simple Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        for (String group : paren_string.split(" ")) {
            int level = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    level++;
                } else if (c == ')') {
                    level--;
                }
            }
            result.add(level);
        }
        return result;
    }
}
```

This solution works by iterating over each group in the input string, and for each group, it iterates over each character in the group. If a character is a '(', it increments the level of nesting. If a character is a ')', it decrements the level of nesting. The final level of nesting for each group is added to the result list.

This solution has a time complexity of O(n), where n is the total number of characters in the input string, because it iterates over each character in the string. The space complexity is O(1), because it uses a constant amount of space to store the result list and other variables. 