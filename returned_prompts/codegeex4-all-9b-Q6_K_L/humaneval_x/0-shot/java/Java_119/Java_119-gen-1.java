You can use a stack to solve this problem. Iterate through the characters in the combined string. If you encounter an open parenthesis, push it onto the stack. If you encounter a close parenthesis, check if the stack is empty. If it is, it means there's no corresponding open parenthesis, so the string is not good. If the stack is not empty, pop the top element from the stack. At the end, if the stack is empty, it means all parentheses are balanced, so the string is good. Otherwise, it's not good.

Here's the Java code:

```java
public String matchParens(List<String> lst) {
    Stack<Character> stack = new Stack<>();
    String combined = lst.get(0) + lst.get(1);
    for (char c : combined.toCharArray()) {
        if (c == '(') {
            stack.push(c);
        } else if (c == ')') {
            if (stack.isEmpty()) {
                return "No";
            } else {
                stack.pop();
            }
        }
    }
    return stack.isEmpty() ? "Yes" : "No";
}
```

This code first creates a stack and combines the two strings. Then it iterates through the combined string, pushing open parentheses onto the stack and popping them when a close parenthesis is encountered. If a close parenthesis is encountered when the stack is empty, it means there's no corresponding open parenthesis, so the string is not good. Finally, it checks if the stack is empty. If it is, it means all parentheses are balanced, so the string is good. Otherwise, it's not good.