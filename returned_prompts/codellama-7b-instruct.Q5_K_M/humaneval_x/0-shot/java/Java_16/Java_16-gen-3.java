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
        int distinctCharacters = 0;
        Set<Character> set = new HashSet<>();
        for (char c : string.toCharArray()) {
            if (!set.contains(c)) {
                set.add(c);
                distinctCharacters++;
            }
        }
        return distinctCharacters;
    }
}