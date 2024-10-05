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
        Set<Character> distinctCharacters = new HashSet<>();
        for (char c : string.toCharArray()) {
            distinctCharacters.add(Character.toLowerCase(c));
        }
        return distinctCharacters.size();
    }
}