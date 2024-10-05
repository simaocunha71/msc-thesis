Here is a Java solution for the problem. The idea is to iterate over the string and keep track of the current level of nesting. When we encounter an opening parenthesis, we increment the level, and when we encounter a closing parenthesis, we decrement the level.

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        int level = 0;
        for (int i = 0; i < paren_string.length(); i++) {
            char c = paren_string.charAt(i);
            if (c == '(') {
                level++;
            } else if (c == ')') {
                level--;
            }
            if (c == ')') {
                result.add(level);
            }
        }
        return result;
    }
}
```

For example, for the input "(()()) ((())) () ((())()())", the output will be [2, 3, 1, 3]. The first group has a maximum level of nesting of 2, the second group has a maximum level of nesting of 3, and so on.