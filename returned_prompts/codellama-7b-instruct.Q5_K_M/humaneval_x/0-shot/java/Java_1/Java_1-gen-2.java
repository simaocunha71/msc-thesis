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
        List<String> groups = new ArrayList<String>();
        int open = 0;
        int close = 0;
        int start = 0;
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                open++;
            } else if (paren_string.charAt(i) == ')') {
                close++;
            }
            if (open == close) {
                groups.add(paren_string.substring(start, i + 1));
                start = i + 1;
            }
        }
        return groups;
    }
}
