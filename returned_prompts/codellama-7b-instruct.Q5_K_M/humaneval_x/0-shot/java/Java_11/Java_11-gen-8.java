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

        char[] result = new char[a.length()];
        for (int i = 0; i < a.length(); i++) {
            result[i] = (a.charAt(i) ^ b.charAt(i)) + "";
        }
        return String.valueOf(result);
    }
}