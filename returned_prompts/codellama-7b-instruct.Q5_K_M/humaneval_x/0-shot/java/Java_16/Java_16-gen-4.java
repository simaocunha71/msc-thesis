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
        int count = 0;
        Set<Character> characters = new HashSet<Character>();
        for (char c : string.toCharArray()) {
            characters.add(c);
        }
        return characters.size();
    }
}