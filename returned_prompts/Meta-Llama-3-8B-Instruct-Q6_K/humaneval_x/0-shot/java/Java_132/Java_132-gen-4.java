Here is the Java code that implements the function:

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

This code uses a stack to keep track of the opening brackets. When an opening bracket is encountered, it is pushed onto the stack. When a closing bracket is encountered, the top of the stack is checked. If the stack is empty, it means there is no matching opening bracket, so the function returns false. If the stack is not empty, the top element is popped off the stack. After going through the entire string, the function checks if the stack is empty. If it is, it means all brackets were properly matched, so the function returns false. If the stack is not empty, it means there are unmatched opening brackets, so the function returns true.

The time complexity of this code is O(n), where n is the length of the input string. This is because it goes through the string once. The space complexity is also O(n), as in the worst case, all characters in the string could be opening brackets, so the stack would contain all of them. 