import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> stringXor("010", "110")
    "100"
     */
    public String stringXor(String a, String b) {
        int length = Math.min(a.length(), b.length());
        StringBuilder res = new StringBuilder();

        for (int i = 0; i < length; i++) {
            char c = a.charAt(i);
            char d = b.charAt(i);
            
            if ((c & d) == 0)
                res.append("1");
            else
                res.append("0");
        }
        
        return res.toString();
    }
}
