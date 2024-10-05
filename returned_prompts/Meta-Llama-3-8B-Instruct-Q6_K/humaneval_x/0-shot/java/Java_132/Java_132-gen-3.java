Here is a Java solution for the problem:

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
            stack.pop();
        }
    }
    return !stack.isEmpty();
}
```

In this solution, we use a stack to keep track of the opening brackets. For each character in the string, if it's an opening bracket, we push it to the stack. If it's a closing bracket, we pop the top element from the stack. If the stack is empty when we encounter a closing bracket, it means there's no matching opening bracket, so we return false. After iterating through the entire string, if the stack is not empty, it means there are unmatched opening brackets, so we return true. Otherwise, we return false. This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.