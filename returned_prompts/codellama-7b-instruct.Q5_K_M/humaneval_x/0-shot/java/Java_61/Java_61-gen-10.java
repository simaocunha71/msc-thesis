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

        int len = brackets.length();
        if (len == 0) return true;

        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < len; i++) {
            if (brackets.charAt(i) == '(') {
                stack.push(brackets.charAt(i));
            } else if (stack.empty()) {
                return false;
            } else {
                stack.pop();
            }
        }

        return stack.empty();
    }
}
