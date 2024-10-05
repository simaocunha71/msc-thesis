Here is the Java solution for the problem:

```java
import java.util.Stack;

class Solution {
    public boolean correctBracketing(String brackets) {
        Stack<Character> stack = new Stack<>();
        for (char bracket : brackets.toCharArray()) {
            if (bracket == '(') {
                stack.push(')');
            } else if (bracket == ')') {
                if (stack.isEmpty() || stack.pop() != ')') {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
```

In this solution, we use a Stack to keep track of the opening brackets. When we encounter an opening bracket, we push the corresponding closing bracket onto the stack. When we encounter a closing bracket, we check if the stack is empty (which would mean there's no matching opening bracket) or if the top of the stack is not the expected closing bracket (which would mean there's a mismatch). If either of these conditions is true, we return false. After processing all brackets, we check if the stack is empty. If it is, that means every opening bracket had a corresponding closing bracket, so we return true. If the stack is not empty, that means there were unmatched opening brackets, so we return false.