import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        String[] groups = paren_string.split(" ");
        List<Integer> result = new ArrayList<>();
        for (String group : groups) {
            int level = 0, maxLevel = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    level++;
                    maxLevel = Math.max(level, maxLevel);
                } else if (c == ')') {
                    level--;
                }
            }
            result.add(maxLevel);
        }
        return result;
    }
}