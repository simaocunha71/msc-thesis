import java.util.*;
import java.lang.*;

class Solution {
    public int countDistinctCharacters(String string) {
        Set<Character> distinctChars = new HashSet<>();
        for (char c : string.toCharArray()) {
            distinctChars.add(Character.toLowerCase(c));
        }
        return distinctChars.size();
    }
}