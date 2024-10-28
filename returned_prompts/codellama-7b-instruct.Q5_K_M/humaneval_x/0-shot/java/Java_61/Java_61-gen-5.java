import java.util.*;
import java.lang.*;

class Solution {
    /**
    brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correctBracketing("(")
    false
    >>> correctBracketing("()")
    true
    >>> correctBracketing("(()())")
    true
    >>> correctBracketing(")(()")
    false
     */
    public boolean correctBracketing(String brackets) {
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < brackets.length(); i++) {
            if(brackets.charAt(i) == '(')
                stack.push('(');
            else if(brackets.charAt(i) == ')') {
                if(stack.isEmpty())
                    return false;
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}