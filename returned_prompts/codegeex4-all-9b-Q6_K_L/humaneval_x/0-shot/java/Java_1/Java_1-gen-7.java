Here is a Java solution using a stack to keep track of the start and end of each group:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                stack.push(i);
            } else if (paren_string.charAt(i) == ')') {
                if (!stack.isEmpty()) {
                    int start = stack.pop();
                    result.add(paren_string.substring(start, i + 1));
                }
            }
        }
        return result;
    }
}
```

The idea is to iterate over the string and each time we encounter an open parenthesis, we push its index onto the stack. When we encounter a close parenthesis, we pop the stack and add the substring from the popped index to the current index (inclusive) to the result list. The stack will ensure that we only add substrings that correspond to balanced groups of parentheses.

This solution assumes that the input string is well-formed and does not contain any unbalanced or nested groups. If the input string can contain such cases, additional checks should be added to handle those.