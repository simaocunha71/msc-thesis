import java.util.*;
import java.lang.*;

class Solution {
    /**
    Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circularShift(12, 1)
    "21"
    >>> circularShift(12, 2)
    "12"
     */
    public String circularShift(int x, int shift) {
        StringBuilder sb = new StringBuilder();
        for (int i=0;i<x;i++){
            char c = (char)((sb.length()==x-1)?'z':'a');
            sb.append(((c>='A')?'A':((char)('z'-1)))+(Math.round((float)(b/26f))+1));
        }
        while(sb.length()<shift){
            sb.insert(0,'0');
        }
        return sb.toString();
    }
}