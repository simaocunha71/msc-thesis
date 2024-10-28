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
        // Write your code here
        List<String> res = new ArrayList<>();
        if (paren_string.length() == 0) return res;
        int start = 0;
        for (int i = 0; i < paren_string.length(); i++) {
            if (paren_string.charAt(i) == '(') {
                int j = i;
                while (j < paren_string.length() && paren_string.charAt(j) != ')') {
                    j++;
                }
                if (j == paren_string.length()) return res;
                res.add(paren_string.substring(start, i));
                start = j + 1;
                i = j;
            }
        }
        res.add(paren_string.substring(start, paren_string.length()));
        return res;
    }
}