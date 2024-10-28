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
        // Write your code here
        Stack<Character> stack = new Stack<Character>();
        for(int i=0; i<brackets.length();i++){
            if(brackets.charAt(i) == '('){
                stack.push(brackets.charAt(i));
            }
            else{
                if(stack.isEmpty())
                    return false;
                else
                    stack.pop();
            }
        }
        if(!stack.isEmpty())
            return false;
        return true;
    }
}
