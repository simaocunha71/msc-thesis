import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseNestedParens(String paren_string) {
        String[] groups = paren_string.split(" ");
        List<Integer> result = new ArrayList<>();
        for (String group : groups) {
            int maxDepth = 0;
            int currentDepth = 0;
            for (char c : group.toCharArray()) {
                if (c == '(') {
                    currentDepth++;
                    maxDepth = Math.max(maxDepth, currentDepth);
                } else if (c == ')') {
                    currentDepth--;
                }
            }
            result.add(maxDepth);
        }
        return result;
    }
}