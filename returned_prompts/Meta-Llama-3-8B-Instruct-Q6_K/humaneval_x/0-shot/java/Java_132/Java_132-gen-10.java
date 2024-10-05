Here is a Java solution that uses a stack to solve this problem:

```java
import java.util.*;

class Solution {
    public boolean isNested(String string) {
        Stack<Character> stack = new Stack<>();
        for (char c : string.toCharArray()) {
            if (c == '[') {
                stack.push(c);
            } else if (c == ']') {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return !stack.isEmpty();
    }
}
```

This solution works by iterating over the input string and pushing opening brackets onto a stack. When a closing bracket is encountered, the top element of the stack is popped if it's not empty. If the stack is empty when a closing bracket is encountered, it means there's no matching opening bracket, so the function returns false. At the end of the function, if the stack is not empty, it means there are unmatched opening brackets, so the function returns true. If the stack is empty, it means all brackets are properly matched, so the function returns false.