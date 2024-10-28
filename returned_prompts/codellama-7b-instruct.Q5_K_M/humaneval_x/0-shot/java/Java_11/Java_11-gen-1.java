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
        StringBuilder sb = new StringBuilder();
        int carry = 0, i = a.length() - 1, j = b.length() - 1;
        while(i >= 0 || j >= 0 || carry == 1){
            int aVal = i >= 0 ? a.charAt(i) - '0' : 0;
            int bVal = j >= 0 ? b.charAt(j) - '0' : 0;
            int xorVal = aVal ^ bVal ^ carry;
            sb.append(xorVal);
            carry = aVal ^ bVal;
            i--; j--;
        }
        return sb.reverse().toString();
    }
}





