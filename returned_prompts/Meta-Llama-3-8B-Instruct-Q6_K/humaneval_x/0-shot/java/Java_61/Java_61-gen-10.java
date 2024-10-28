Here is a simple solution in Java that uses a Stack to keep track of the opening brackets:

```java
import java.util.*;

class Solution {
    public boolean correctBracketing(String brackets) {
        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}
```

This solution works by iterating over the string and pushing each opening bracket onto the stack. When a closing bracket is encountered, it checks if the stack is empty (which means there's no matching opening bracket) or pops the opening bracket from the stack. After iterating over the entire string, it checks if the stack is empty. If it is, that means every opening bracket had a corresponding closing bracket, so it returns true. If the stack is not empty, that means there were some unmatched opening brackets, so it returns false.