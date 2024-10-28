Here is a Java solution to the problem. It uses a stack to keep track of the parentheses and the current nesting level. When it encounters a closing parenthesis, it pops the stack and decrements the current nesting level. When it encounters an opening parenthesis, it pushes the current nesting level onto the stack and increments the current nesting level.

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        int maxLevel = 0;
        int level = 0;
        for (String group : paren_string.split(" ")) {
            level = 0;
            Stack<Integer> stack = new Stack<>();
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    stack.push(level);
                    level++;
                } else if (c == ')') {
                    level = stack.pop();
                }
            }
            result.add(level);
            maxLevel = Math.max(maxLevel, level);
        }
        return result;
    }
}
```

This solution has a time complexity of O(n), where n is the total number of characters in the input string, and a space complexity of O(n), where n is the maximum number of parentheses in any group. The maximum number of parentheses in any group is bounded by the maximum nesting level, which is at most the length of the input string. Therefore, the space complexity is O(n). The time complexity is O(n) because we are processing each character in the input string once. The space complexity is also O(n) because we are storing the nesting level of each group in the result list and the maximum nesting level in the variable maxLevel.