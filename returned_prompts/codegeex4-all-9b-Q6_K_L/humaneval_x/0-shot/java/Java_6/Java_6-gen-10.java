import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        List<Integer> result = new ArrayList<>();
        String[] groups = paren_string.split(" ");
        for (String group : groups) {
            int depth = 0;
            int maxDepth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    depth++;
                    maxDepth = Math.max(depth, maxDepth);
                } else if (c == ')') {
                    depth--;
                }
            }
            result.add(maxDepth);
        }
        return result;
    }
}