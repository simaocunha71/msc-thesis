Here is a simple Java solution using a stack. The idea is to traverse the string and for every opening bracket push it into the stack. For every closing bracket, check if the stack is empty. If it is, then the brackets are not balanced so return false. If it is not, then pop an opening bracket from the stack. If at the end the stack is not empty, then the brackets are not balanced so return false. Otherwise, return true.

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean correctBracketing(String brackets) {
        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.isEmpty()) {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        return stack.isEmpty();
    }
}
```