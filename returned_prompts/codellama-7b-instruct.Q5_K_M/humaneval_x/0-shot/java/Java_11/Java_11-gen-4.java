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

        String result = "";
        for(int i = 0; i < a.length(); i++)
        {
            if(a.charAt(i) == '1' && b.charAt(i) == '1')
                result += "0";
            else
                result += "1";
        }
        return result;
    }
}

