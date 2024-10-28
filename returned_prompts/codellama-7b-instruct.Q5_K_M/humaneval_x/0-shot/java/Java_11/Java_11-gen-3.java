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

        if (a.length() != b.length()) {
            throw new IllegalArgumentException("a and b must be of same length");
        }
        String result = "";
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(i)) {
                result += a.charAt(i);
            } else {
                result += (a.charAt(i) == '1' ? '0' : '1');
            }
        }
        return result;
    }
}
