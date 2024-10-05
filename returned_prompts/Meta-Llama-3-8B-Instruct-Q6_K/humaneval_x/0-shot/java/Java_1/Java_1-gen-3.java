Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int open = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                open++;
                sb.append(c);
            } else if (c == ')') {
                open--;
                sb.append(c);
                if (open == 0) {
                    result.add(sb.toString());
                    sb.setLength(0);
                }
            }
        }
        return result;
    }
}
```

This solution iterates over the input string and uses a `StringBuilder` to build up the current group of parentheses. When it encounters a closing parenthesis and the current group is complete (i.e., `open` is 0), it adds the group to the result list and resets the `StringBuilder`. The time complexity is O(n), where n is the length of the input string. The space complexity is O(n), where n is the maximum length of a group of parentheses in the input string. 