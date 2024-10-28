```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean correctBracketing(String brackets) {
        if (brackets.length() % 2 != 0) return false;
        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                stack.push(c);
            } else if (c == '>') {
                if (stack.isEmpty() || stack.pop() != '<') return false;
            }
        }
        return stack.isEmpty();
    }
}
```