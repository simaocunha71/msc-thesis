import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int count = 0;
        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                count++;
                sb.append(c);
            } else if (c == ')') {
                count--;
                sb.append(c);
                if (count == 0) {
                    result.add(sb.toString());
                    sb.setLength(0);
                }
            }
        }
        return result;
    }
}