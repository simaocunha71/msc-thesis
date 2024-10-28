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
        int openBracketCount = 0;
        for (int i = 0; i < brackets.length(); i++) {
            if (brackets.charAt(i) == '<') {
                openBracketCount++;
            } else if (brackets.charAt(i) == '>') {
                openBracketCount--;
            }
            if (openBracketCount < 0) {
                return false;
            }
        }
        return openBracketCount == 0;
    }
}

