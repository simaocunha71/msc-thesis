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
        if (string == null || string.isEmpty()) {
            return 0;
        }
        Set<Character> uniqueChars = new HashSet<>();
        for (char c : string.toCharArray()) {
            uniqueChars.add(Character.toLowerCase(c));
        }
        return uniqueChars.size();
    }
}