You can use a stack to solve this problem. Iterate through the string and push each "<" onto the stack. Whenever you encounter a ">", check if the stack is empty. If it is, return false because there's no corresponding opening bracket. If the stack is not empty, pop an element from the stack. If the stack becomes empty before you finish iterating through the string, return false. Otherwise, return true.

Here's the Java code:

```java
import java.util.*;

class Solution {
    public boolean correctBracketing(String brackets) {
        Stack<Character> stack = new Stack<>();
        for (char c : brackets.toCharArray()) {
            if (c == '<') {
                stack.push(c);
            } else if (c == '>') {
                if (stack.isEmpty()) {
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}
```

The time complexity of this algorithm is O(n), where n is the length of the input string.