Here is the Java code to solve this problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isNested(String string) {
        Stack<Character> stack = new Stack<>();
        for (char c : string.toCharArray()) {
            if (c == '[') {
                stack.push(c);
            } else if (c == ']') {
                if (stack.isEmpty() || stack.peek() != '[') {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        return stack.size() > 1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.isNested("[[]]")); // true
        System.out.println(solution.isNested("[]]]]]]][[[[[]")); // false
        System.out.println(solution.isNested("[][]")); // false
        System.out.println(solution.isNested("[]")); // false
        System.out.println(solution.isNested("[[][]]")); // true
        System.out.println(solution.isNested("[[]][[)); // true
    }
}
```
This code uses a stack to keep track of the opening brackets. When a closing bracket is encountered, it checks if the top of the stack is an opening bracket. If it is, then the brackets are nested and the function returns true. If the top of the stack is not an opening bracket, then the brackets are not nested and the function returns false. If the stack is not empty at the end of the function, then there are unmatched opening brackets and the function returns false.