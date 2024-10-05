Here is a simple way to solve this problem using a stack:

```java
import java.util.*;

class Solution {
    public boolean isNested(String string) {
        Stack<Character> stack = new Stack<>();
        for (char c : string.toCharArray()) {
            if (c == '[') {
                stack.push(c);
            } else if (c == ']') {
                if (!stack.isEmpty() && stack.peek() == '[') {
                    stack.pop();
                    if (!stack.isEmpty() && stack.peek() == '[') {
                        return true;
                    }
                } else {
                    return false;
                }
            }
        }
        return false;
    }
}
```

The idea is to iterate through the string and keep track of the brackets using a stack. If we encounter an opening bracket, we push it onto the stack. If we encounter a closing bracket, we check if the top of the stack is an opening bracket. If it is, we pop the stack and check if the new top of the stack is an opening bracket. If it is, we return true. If at any point we encounter a closing bracket and the top of the stack is not an opening bracket, we return false. If we finish iterating through the string and the stack is empty, we return false.