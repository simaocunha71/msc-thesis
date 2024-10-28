Here is a Java solution that uses a stack to keep track of the brackets. If a closing bracket is found, it checks if there is a corresponding opening bracket on the stack. If there is, it pops the opening bracket from the stack. If there is no corresponding opening bracket, it pushes the closing bracket onto the stack. Finally, it checks if the stack is empty and contains more than one bracket. If it does, it means there is a nested subsequence.

```java
import java.util.*;

class Solution {
    public boolean isNested(String string) {
        Stack<Character> stack = new Stack<>();
        for (char c : string.toCharArray()) {
            if (c == ']') {
                if (stack.isEmpty() || stack.pop() != '[') {
                    stack.push(']');
                }
            } else {
                stack.push('[');
            }
        }
        return !stack.isEmpty() && stack.size() > 1;
    }
}
```

This solution has a time complexity of O(n) where n is the length of the input string.