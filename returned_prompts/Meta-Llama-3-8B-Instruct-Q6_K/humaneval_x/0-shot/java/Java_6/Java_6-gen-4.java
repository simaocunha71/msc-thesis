Here is the Java code that uses a stack to solve the problem. It iterates over the string, pushing opening parentheses onto the stack and popping them off when a closing parenthesis is encountered. It keeps track of the maximum nesting level seen so far and updates it whenever it encounters a deeper level of nesting.

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        int maxLevel = 0;
        int currentLevel = 0;
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                currentLevel++;
                maxLevel = Math.max(maxLevel, currentLevel);
            } else if (c == ')') {
                currentLevel--;
            }
        }
        result.add(maxLevel);
        return result;
    }
}
```

This code iterates over the input string only once, so its time complexity is O(n), where n is the length of the input string. The space complexity is O(1) because it uses a constant amount of space to store the result, the maximum level, and the current level.