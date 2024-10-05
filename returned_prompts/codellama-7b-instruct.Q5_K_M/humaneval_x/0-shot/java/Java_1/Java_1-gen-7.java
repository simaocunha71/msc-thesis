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
        List<String> paren_groups = new ArrayList<String>();
        Stack<Character> stack = new Stack<Character>();
        String current_group = "";
        for(int i = 0; i < paren_string.length(); i++) {
            char c = paren_string.charAt(i);
            if(c == '(')
                stack.push(c);
            else if(c == ')')
                stack.pop();
            else if(c == ' ')
                continue;
            else
                current_group += c;
            if(stack.isEmpty()) {
                paren_groups.add(current_group);
                current_group = "";
            }
        }
        return paren_groups;
    }
}
