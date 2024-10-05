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

        List<String> result = new ArrayList<String>();
        if (paren_string.length() == 0) {
            return result;
        }
        int open_count = 0;
        int last_open = -1;
        int last_close = -1;
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                if (open_count == 0) {
                    last_open = i;
                }
                open_count++;
            } else if (paren_string.charAt(i) == ')') {
                open_count--;
                if (open_count == 0) {
                    last_close = i;
                    result.add(paren_string.substring(last_open + 1, last_close));
                    last_open = last_close;
                } else if (open_count < 0) {
                    return new ArrayList<String>();
                }
            }
        }
        if (open_count != 0) {
            return new ArrayList<String>();
        }
        return result;
    }
}
