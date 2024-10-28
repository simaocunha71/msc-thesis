```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean correctBracketing(String brackets) {
        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                stack.push(c);
            } else {
                if (stack.isEmpty() || stack.pop() != '<') {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
```