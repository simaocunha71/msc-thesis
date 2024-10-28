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
        // write your code here
        if(words == null || words.size() == 0)
            return "";
        int max = 0;
        String res = "";
        for(String word : words)
        {
            if(word.length() > max)
            {
                max = word.length();
                res = word;
            }
            else if(word.length() == max)
            {
                if(word.compareTo(res) < 0)
                    res = word;
            }
        }
        return res;
    }
}
