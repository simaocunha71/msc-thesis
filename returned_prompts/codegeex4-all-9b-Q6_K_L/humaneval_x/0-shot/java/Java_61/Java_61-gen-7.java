Here is a simple way to solve this problem using a stack data structure:

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
                if (stack.isEmpty() || stack.pop() != '(') {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}
```

The idea is to iterate through the string and whenever we encounter an opening bracket, we push it to the stack. If we encounter a closing bracket, we check if the stack is empty or if the top element of the stack is not an opening bracket. If either of these conditions is true, we return false. At the end of the loop, we check if the stack is empty. If it is not, it means there are unmatched opening brackets, so we return false. If it is empty, we return true.