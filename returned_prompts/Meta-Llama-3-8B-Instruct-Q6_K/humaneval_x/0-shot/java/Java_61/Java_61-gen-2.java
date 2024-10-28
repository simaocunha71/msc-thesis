Here is the solution:
```java
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
```
Explanation:

* We use a stack to keep track of the opening brackets.
* For each character in the input string, we check if it's an opening bracket ( '(' ). If it is, we push the corresponding closing bracket ( ')' ) onto the stack.
* If the character is a closing bracket ( ')' ), we check if the stack is empty or if the top of the stack doesn't match the closing bracket. If either condition is true, we return false.
* After processing all characters, we check if the stack is empty. If it is, that means every opening bracket had a corresponding closing bracket, so we return true. If the stack is not empty, that means there were unmatched opening brackets, so we return false.

This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n), where n is the number of opening brackets in the input string.