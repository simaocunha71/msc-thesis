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
        // Create a HashSet to store unique characters
        HashSet<Character> set = new HashSet<Character>();

        // Loop through each character in the string
        for (char c : string.toCharArray()) {

            // Convert character to upper case and check if it is already in the HashSet
            // if not then add it to the HashSet
            if (!set.contains(Character.toUpperCase(c))) {
                set.add(Character.toUpperCase(c));
                count++;
            }
        }

        return count;
    }
}
