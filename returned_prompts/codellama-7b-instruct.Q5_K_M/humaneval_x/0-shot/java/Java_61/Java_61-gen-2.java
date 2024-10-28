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
        int open = 0;
        int close = 0;
        for (char c : brackets.toCharArray()) {
            if (c == '(') open++;
            else if (c == ')') close++;
        }
        return open == close;
    }
}



