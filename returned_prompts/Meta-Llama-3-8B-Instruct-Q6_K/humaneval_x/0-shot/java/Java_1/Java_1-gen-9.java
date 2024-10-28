Here is a Java solution for this problem:

```java
import java.util.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                sb.append(c);
            } else if (c == ')') {
                if (sb.length() > 0 && sb.charAt(sb.length() - 1) == '(') {
                    sb.deleteCharAt(sb.length() - 1);
                } else {
                    result.add(sb.toString());
                    sb = new StringBuilder();
                }
            } else {
                sb.append(c);
            }
        }
        if (sb.length() > 0) {
            result.add(sb.toString());
        }
        return result;
    }
}
```

This solution iterates over the input string, maintaining a `StringBuilder` to collect characters until it encounters a `')'` character. If the last character in the `StringBuilder` is an open parenthesis, it means we've found a complete group, so we add the group to the result list and reset the `StringBuilder`. If the last character in the `StringBuilder` is not an open parenthesis, we add the group to the result list and reset the `StringBuilder`. At the end, we add the last group to the result list if it's not empty. 

The time complexity of this solution is O(n), where n is the length of the input string. The space complexity is also O(n), as in the worst case, the `StringBuilder` can contain n characters. 