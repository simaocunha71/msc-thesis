Here is a Java solution using a stack:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        String[] groups = paren_string.split(" ");
        List<Integer> res = new ArrayList<>();
        for (String group : groups) {
            int level = 0, maxLevel = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    level++;
                    maxLevel = Math.max(maxLevel, level);
                } else if (c == ')') {
                    level--;
                }
            }
            res.add(maxLevel);
        }
        return res;
    }
}
```

The idea is to go through each group of parentheses. For each group, we maintain a counter for the current level of nesting and a maximum level. When we encounter an opening parenthesis, we increase the level and update the maximum level if necessary. When we encounter a closing parenthesis, we decrease the level. At the end, we add the maximum level to our result list.

Here is a simple test case:

```java
Solution sol = new Solution();
assert sol.parseNestedParens("(()()) ((())) () ((())()())").equals(Arrays.asList(2, 3, 1, 3));
```

Note that we use the `assert` keyword to check that the result of the `parseNestedParens` method matches the expected result. If the result does not match the expected result, the program will throw an `AssertionError`.