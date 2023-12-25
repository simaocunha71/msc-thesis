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
        if (s == null || s.length() <= 0) return -1;
            
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
         for (int i=0 ;i<s.length();i++) {
            char c = s.charAt(i);
            if (!map.containsKey(c)) 
                map.put(c,1);
         }
        int count = 0;
        for (Character c : map.keySet())
        {
            if ((int) c >9) //uppercase vowels are A,E,I and O
                count+=map.get((int) c);
        }
        return count;
    } 
}