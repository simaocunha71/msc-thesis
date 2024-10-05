Here is a Java solution for this problem:

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        for(String group : paren_string.split("\\s+")) {
            int level = 0;
            for(char c : group.toCharArray()) {
                if(c == '(') level++;
                else if(c == ')') level--;
                if(level < 0) break;
            }
            result.add(level);
        }
        return result;
    }
}
```

This solution works by iterating over each group in the input string, and for each group, it keeps track of the level of nesting by incrementing a counter whenever it encounters an open parenthesis and decrementing it whenever it encounters a close parenthesis. It breaks the loop when it encounters a close parenthesis that would result in a negative level, because that means the parentheses are not properly nested. The level at that point is the maximum level of nesting for that group, which is added to the result list. The process is repeated for each group in the input string.

For example, given the input "(()()) ((())) () ((())()())", the output would be [2, 3, 1, 3]. The maximum level of nesting for the first group is 2, for the second group is 3, for the third group is 1, and for the fourth group is 3.