Here is a simple solution in Java:

```java
public boolean correctBracketing(String brackets) {
    Stack<Character> stack = new Stack<>();
    for (char bracket : brackets.toCharArray()) {
        if (bracket == '(') {
            stack.push(bracket);
        } else if (bracket == ')') {
            if (stack.isEmpty()) {
                return false; // no matching opening bracket
            }
            stack.pop();
        }
    }
    return stack.isEmpty(); // all brackets are matched
}
```

This solution uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if the stack is empty. If the stack is empty, it means there is no matching opening bracket, so it returns false. If the stack is not empty, it pops the opening bracket from the stack. Finally, it checks if the stack is empty. If the stack is empty, it means all brackets are matched, so it returns true. If the stack is not empty, it means there are unmatched opening brackets, so it returns false.