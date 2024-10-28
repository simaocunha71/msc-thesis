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
        int n = a.length();
        String res = "";
        for (int i = 0; i < n; i++) {
            res += (a.charAt(i) ^ b.charAt(i)) + "";
        }
        return res;
    }
}
