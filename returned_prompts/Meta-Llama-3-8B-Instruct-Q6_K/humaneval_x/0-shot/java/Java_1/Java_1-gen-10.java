Here is a solution that uses a stack to keep track of the parentheses and a StringBuilder to build the separate groups:

```java
import java.util.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        Stack<Character> stack = new Stack<>();

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                stack.push(c);
                sb.append(c);
            } else if (c == ')') {
                if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                    sb.append(c);
                    if (stack.isEmpty()) {
                        result.add(sb.toString());
                        sb = new StringBuilder();
                    }
                } else {
                    sb.append(c);
                }
            }
        }
        return result;
    }
}
```

This solution iterates through the input string, pushing each open parenthesis onto the stack and appending it to the current group. When it encounters a close parenthesis, it pops the stack if the top of the stack is an open parenthesis, and appends the close parenthesis to the current group. If the stack becomes empty after popping, it means we have found a complete group, so we add the current group to the result list and reset the current group. Finally, we return the result list.

For example, given the input string "( ) (( )) (( )( ))", the function will return the list ["()", "(())", "(()())"].