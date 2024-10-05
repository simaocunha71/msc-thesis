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
        // Write your code here
        Set<Character> set = new HashSet<Character>();
        for (char c : string.toLowerCase().toCharArray()) {
            set.add(c);
        }
        return set.size();
    }
}

