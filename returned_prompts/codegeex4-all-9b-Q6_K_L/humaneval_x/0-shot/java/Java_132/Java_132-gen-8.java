```java
public boolean isNested(String string) {
    Stack<Character> stack = new Stack<>();
    for (int i = 0; i < string.length(); i++) {
        char c = string.charAt(i);
        if (c == '[') {
            stack.push(c);
        } else if (c == ']') {
            if (stack.isEmpty()) {
                return false;
            } else {
                stack.pop();
                if (stack.isEmpty()) {
                    return true;
                }
            }
        }
    }
    return false;
}
```