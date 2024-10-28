import java.util.*;
import java.lang.*;

class Solution {
    /**
    brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.
    
    >>> correctBracketing("<")
    false
    >>> correctBracketing("<>")
    true
    >>> correctBracketing("<<><>>")
    true
    >>> correctBracketing("><<>")
    false
     */
    public boolean correctBracketing(String brackets) {

        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < brackets.length(); i++) {
            char bracket = brackets.charAt(i);
            if (bracket == '<') {
                stack.push(bracket);
            } else if (bracket == '>') {
                if (stack.empty()) return false;
                stack.pop();
            }
        }
        return stack.empty();
    }
}














