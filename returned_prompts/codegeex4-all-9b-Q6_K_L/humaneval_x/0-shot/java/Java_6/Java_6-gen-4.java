import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parseNestedParens("(()()) ((())) () ((())()())")
    [2, 3, 1, 3]
     */
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> levels = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int level = 0;
            int maxLevel = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    level++;
                    maxLevel = Math.max(level, maxLevel);
                } else if (c == ')') {
                    level--;
                }
            }
            levels.add(maxLevel);
        }
        return levels;
    }
}