import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        List<String> result = new ArrayList<>();
        String currentGroup = "";
        int balance = 0;

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                balance++;
                currentGroup += c;
            } else if (c == ')') {
                balance--;
                currentGroup += c;
                if (balance == 0) {
                    result.add(currentGroup);
                    currentGroup = "";
                }
            }
        }

        return result;
    }
}