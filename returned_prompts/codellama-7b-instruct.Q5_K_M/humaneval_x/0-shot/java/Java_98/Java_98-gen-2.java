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

        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0 && isVowel(s.charAt(i)) && isUpper(s.charAt(i))) {
                count++;
            }
        }
        return count;
    }
    
    public boolean isVowel(char c) {
        switch (c) {
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
            case 'Y':
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'y':
                return true;
            default:
                return false;
        }
    }
    
    public boolean isUpper(char c) {
        return c >= 'A' && c <= 'Z';
    }
}
