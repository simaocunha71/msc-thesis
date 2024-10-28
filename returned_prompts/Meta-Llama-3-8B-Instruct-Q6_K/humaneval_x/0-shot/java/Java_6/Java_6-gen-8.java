Here is the Java solution for the problem. The idea is to iterate over the string and whenever we encounter an opening parenthesis, we increase the level of nesting. Whenever we encounter a closing parenthesis, we decrease the level of nesting. The maximum level of nesting in a group is stored in the list and returned as the result.

```java
import java.util.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        int currentMax = 0;
        int currentLevel = 0;

        for (String group : paren_string.split(" ")) {
            int max = 0;
            int level = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    level++;
                } else if (c == ')') {
                    level--;
                }
                max = Math.max(max, level);
            }
            result.add(max);
            currentMax = Math.max(currentMax, max);
            currentLevel = 0;
        }

        return result;
    }
}
```
This solution works by iterating over each group in the input string, and for each group, it iterates over each character in the group. If the character is an opening parenthesis, it increases the level of nesting; if the character is a closing parenthesis, it decreases the level of nesting. The maximum level of nesting in the group is stored in the list and returned as the result. The maximum level of nesting in all groups is also stored for debugging purposes. The time complexity is O(n), where n is the total number of characters in the input string. The space complexity is O(1), as we only use a constant amount of space to store the result and other variables.