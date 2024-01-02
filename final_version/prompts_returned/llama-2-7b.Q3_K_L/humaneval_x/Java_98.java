import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    countUpper("aBCdEf") returns 1
    countUpper("abcdefg") returns 0
    countUpper("dBBE") returns 0
     */    
    public int countUpper(String s) {
        if (s == null || s.length() == 0) return 0;
        char firstChar = s.charAt(0);
        if (firstChar <= 'Z') firstChar +=26; // change to upper case
        
        int count = 1;
        for (int i=0; i<s.length(); ++i) {
            if (isUpper(s.charAt(i))) {
                if ((i % 2 == 0)) count++;
            } else {
                break;
            }
        }
        
        return count;
    }
    
    static boolean isUpper(char ch) {
        if (ch >= 'a' && ch <= 'z') return false;
        if (ch > 'Z') return true;
        return false;
    }
}