Here is a simple solution using a stack to keep track of the opening brackets. We iterate over the string and for each character, if it is an opening bracket, we push it onto the stack. If it is a closing bracket, we check if the stack is empty or the top of the stack is not the corresponding opening bracket. If either is true, we return false. Finally, if the stack is not empty after iterating through the string, we return false, otherwise we return true.

```java
public boolean correctBracketing(String brackets) {
    Stack<Character> stack = new Stack<>();
    for (char c : brackets.toCharArray()) {
        if (c == '(') {
            stack.push(c);
        } else if (c == ')') {
            if (stack.isEmpty() || stack.pop() != '(') {
                return false;
            }
        }
    }
    return stack.isEmpty();
}
```

The time complexity of this solution is O(n), where n is the length of the input string. The space complexity is also O(n) because in the worst case, we might have to push all the opening brackets onto the stack.