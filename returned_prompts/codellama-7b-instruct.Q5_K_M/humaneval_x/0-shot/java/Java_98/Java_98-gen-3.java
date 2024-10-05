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
    int len = s.length();
    for (int i = 0; i < len; i++) {
        if (i % 2 == 0 && Character.isUpperCase(s.charAt(i))) {
            count++;
        }
    }
    return count;
}

}
