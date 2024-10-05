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
        // write your code here
        int left = 0;
        int right = 0;
        for (int i = 0; i < brackets.length(); i++) {
            if (brackets.charAt(i) == '<') {
                left++;
            } else {
                right++;
            }
        }
        if (left == right) {
            return true;
        } else {
            return false;
        }
    }
}
