Here is a simple and efficient solution in Java:

```java
public boolean correctBracketing(String brackets) {
    Stack<Character> stack = new Stack<>();
    for (char c : brackets.toCharArray()) {
        if (c == '(') {
            stack.push(c);
        } else if (c == ')') {
            if (stack.isEmpty()) {
                return false; // no matching opening bracket
            }
            stack.pop();
        }
    }
    return stack.isEmpty(); // all opening brackets have been matched
}
```

This solution uses a stack to keep track of the opening brackets. For each character in the string, if it's an opening bracket, we push it onto the stack. If it's a closing bracket, we check if the stack is empty. If it is, we return false, because there's no matching opening bracket. If the stack is not empty, we pop the opening bracket from the stack. At the end, we return whether the stack is empty. If it is, that means all opening brackets have been matched, and we return true. If the stack is not empty, that means there are unmatched opening brackets, and we return false.

This solution has a time complexity of O(n), where n is the length of the input string, because we iterate over the string once. The space complexity is O(n) as well, because in the worst case, all characters in the string are opening brackets, so the stack will store n characters. 