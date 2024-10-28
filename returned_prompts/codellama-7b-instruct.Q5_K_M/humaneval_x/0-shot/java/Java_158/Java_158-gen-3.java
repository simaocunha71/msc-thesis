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
        String maxWord = "";
        int maxCount = 0;
        for (String word : words) {
            int count = new HashSet<>(Arrays.asList(word.split(""))).size();
            if (count > maxCount || (count == maxCount && word.compareTo(maxWord) < 0)) {
                maxWord = word;
                maxCount = count;
            }
        }
        return maxWord;
    }
}
