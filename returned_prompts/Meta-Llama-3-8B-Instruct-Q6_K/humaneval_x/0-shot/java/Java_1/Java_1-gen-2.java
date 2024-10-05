Here is the solution using a stack and a StringBuilder:

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

        if (!stack.isEmpty()) {
            result.add(sb.toString());
        }

        return result;
    }
}
```

The idea is to iterate over the input string, pushing open parentheses onto the stack and appending them to the StringBuilder. When we encounter a close parenthesis, we pop the stack and append the close parenthesis to the StringBuilder. If the stack is empty after popping, it means we have a complete group of parentheses, so we add the current StringBuilder to the result list and reset it. At the end, if there are any characters left in the StringBuilder, it means they are not part of any group, so we add them to the result list.

This solution assumes that the input string is well-formed and that the parentheses are balanced. If the input string is malformed, this solution will throw a StackOverflowError. If you want to handle malformed input, you would need to add additional error checking code.