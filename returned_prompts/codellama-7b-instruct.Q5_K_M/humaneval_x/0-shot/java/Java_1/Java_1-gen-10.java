import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separateParenGroups("( ) (( )) (( )( ))")
    ["()", "(())", "(()())"]
     */
    public List<String> separateParenGroups(String paren_string) {
        Stack<Character> stack = new Stack<Character>();
        List<String> groups = new ArrayList<String>();
        int i = 0;
        while (i < paren_string.length()) {
            char c = paren_string.charAt(i);
            if (c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if (stack.empty()) {
                    // error!
                    return null;
                }
                stack.pop();
            } else {
                // ignore space
            }
            i++;
        }
        if (!stack.empty()) {
            // error!
            return null;
        }
        groups.add("");
        i = 0;
        while (i < paren_string.length()) {
            char c = paren_string.charAt(i);
            if (c == '(') {
                groups.add("");
            } else if (c == ')') {
                groups.remove(groups.size() - 1);
            } else {
                groups.get(groups.size() - 1) += c;
            }
            i++;
        }
        return groups;
    }
}