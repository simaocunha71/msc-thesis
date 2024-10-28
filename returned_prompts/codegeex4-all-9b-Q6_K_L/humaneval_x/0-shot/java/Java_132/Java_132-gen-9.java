Here is a Java solution which uses a stack to keep track of the positions of the brackets. The stack is used to keep track of the positions of the opening brackets. When a closing bracket is encountered, it checks if the last opening bracket is nested. If it is, it removes it from the stack and continues. If not, it returns false. If the stack is empty and no nested bracket is found, it returns false. If the stack is not empty after the loop, it means there are unmatched opening brackets, so it returns false. If the stack is empty after the loop, it means all brackets are matched and there is at least one nested bracket, so it returns true. The time complexity is O(n) and the space complexity is O(n).

```
public boolean isNested(String string) {
    Stack<Integer> stack = new Stack<Integer>();
    for (int i = 0; i < string.length(); i++) {
        if (string.charAt(i) == '[') {
            stack.push(i);
        } else if (string.charAt(i) == ']') {
            if (stack.isEmpty() || stack.peek() + 1 != i) {
                return false;
            }
            stack.pop();
        }
    }
    return stack.isEmpty();
}
```

I hope this helps! Please let me know if you have any questions.