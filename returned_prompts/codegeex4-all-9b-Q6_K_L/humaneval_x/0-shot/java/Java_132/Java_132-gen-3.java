Here is a Java solution using a stack data structure:

```java
public boolean isNested(String string) {
    Stack<Character> stack = new Stack<>();
    for (char c : string.toCharArray()) {
        if (c == '[') {
            stack.push(c);
        } else if (c == ']') {
            if (stack.isEmpty()) {
                return false;
            }
            if (stack.peek() == '[') {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
    }
    return stack.size() >= 2;
}
```

The function works by iterating through the string character by character. If it encounters a '[' character, it pushes it onto the stack. If it encounters a ']' character, it checks if the stack is empty or if the top of the stack is not a '[' character. If either of these conditions is true, it returns false because there is no valid subsequence of brackets where at least one bracket is nested. If the top of the stack is a '[' character, it pops it from the stack. If the stack has at least two characters after the loop finishes, it means there is a valid subsequence of brackets where at least one bracket is nested, so it returns true.