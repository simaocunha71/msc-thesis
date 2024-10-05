Here is a possible solution in Java:

```java
public boolean correctBracketing(String brackets) {
    Stack<Character> stack = new Stack<>();
    for (char c : brackets.toCharArray()) {
        if (c == '<') {
            stack.push(c);
        } else if (c == '>') {
            if (stack.isEmpty() || stack.pop() != '<') {
                return false;
            }
        }
    }
    return stack.isEmpty();
}
```

This solution uses a stack to keep track of the opening brackets. When it encounters a closing bracket, it checks if there is a corresponding opening bracket in the stack. If there is not, it returns `false`. If there are no more opening brackets in the stack when it finishes processing the string, it returns `true`. If there are still opening brackets in the stack, it returns `false`.