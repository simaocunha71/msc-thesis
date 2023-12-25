import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
     */
    public int digitSum(String s) {
      if (s.length() == 0) return 0;
       for (char c : s.toCharArray()) {
         if((int)(c - 48) >= 26 && (int)(c - 48) <= 103)
           result += 1 + Integer.valueOf(Character.toString(c)).intValue();   // convert to int and add one
       }
        return result;
    }
}