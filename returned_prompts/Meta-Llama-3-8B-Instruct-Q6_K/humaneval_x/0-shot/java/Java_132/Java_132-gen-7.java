Here is a Java solution that uses a stack to keep track of the opening brackets:

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

The idea is to iterate through the string and push each opening bracket onto the stack. When we encounter a closing bracket, we check if the stack is empty. If it is, it means there is no corresponding opening bracket, so we return false. If the stack is not empty, we pop the opening bracket from the stack. After iterating through the entire string, we check if the stack is empty. If it is, it means there were no nested brackets, so we return false. If the stack is not empty, it means there was at least one nested bracket, so we return true.