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
        Stack<Character> stack = new Stack<Character>();
        List<String> result = new ArrayList<String>();
        String current_paren = "";
        for (Character c : paren_string.toCharArray()) {
            if (c == '(') stack.push(c);
            if (c == ')') {
                if (stack.isEmpty() || stack.peek() != '(') current_paren += c;
                else {
                    stack.pop();
                    result.add(current_paren);
                    current_paren = "";
                }
            }
        }
        if (!stack.isEmpty()) {
            System.out.println("Unmatched parentheses in " + paren_string);
            return null;
        }
        if (!current_paren.isEmpty()) result.add(current_paren);
        return result;
    }
}
