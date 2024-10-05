```java
import java.util.*;

class Solution {
    public boolean correctBracketing(String brackets) {
        Deque<Character> stack = new ArrayDeque<>();
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