import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> stringSequence(0)
    "0"
    >>> stringSequence(5)
    "0 1 2 3 4 5"
     */
    public String stringSequence(int n) {
        // Write your solution here
        // Use a StringBuilder to build the string
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<=n; i++){
            sb.append(i);
            if(i<n){
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}
