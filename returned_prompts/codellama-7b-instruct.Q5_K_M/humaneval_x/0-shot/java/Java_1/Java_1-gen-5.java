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
        StringBuffer current = new StringBuffer();
        int balance = 0;
        for (char c : paren_string.toCharArray()) {
            switch (c) {
                case '(':
                    balance++;
                    current.append(c);
                    break;
                case ')':
                    balance--;
                    current.append(c);
                    if (balance == 0) {
                        result.add(current.toString());
                        current = new StringBuffer();
                    }
                    break;
                default:
                    current.append(c);
            }
        }
        return result;
    }
}
