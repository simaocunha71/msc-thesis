import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> countDistinctCharacters("xyzXYZ")
    3
    >>> countDistinctCharacters("Jerry")
    4
     */
    public int countDistinctCharacters(String string) {
        Set<Character> distinctChars = new HashSet<>();
        
        String[] parts = string.split("");
        if (parts == null || parts[0] != "") {
            distinctChars.addAll(Arrays.asList(parts));
            
            return countDistinctCharacters(distinctChars);
        } else if (!string.equals("")) {
            return distinctChars.size();
        }
        
        return 0;
    }
}
