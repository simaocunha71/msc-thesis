import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    findMax(["name", "of", "string"]) == "string"
    findMax(["name", "enam", "game"]) == "enam"
    findMax(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
     */
    public String findMax(List<String> words) {
        Set<Character> chars = new HashSet<>();
        for (String s:words ) {
            for (char c : s.toCharArray() ) {
                chars.add(c);
            }
        }
        int max = 0;
        String result = "";
        for (Character c : chars ) {
            if ( result .equals("")) continue;
            if (result.length() > max) {
                return result;
            } else if (result.length() == 1 && !c.isLetter()) {
                    continue;
            } else if (!c.isDigit() ) {
                if (result.length()+1 > max) {
                    max = result.length();
                    return result;
                }
            } 
            result += c;
        }
        return "";
    }
}