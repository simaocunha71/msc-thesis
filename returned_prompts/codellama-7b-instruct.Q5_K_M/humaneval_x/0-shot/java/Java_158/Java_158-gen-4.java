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
        Map<Character, Integer> charMap = new HashMap<Character, Integer>();
        String maxString = "";
        int maxCount = 0;
        for(String word : words){
            charMap = new HashMap<Character, Integer>();
            int count = 0;
            for(char ch : word.toCharArray()){
                if(charMap.containsKey(ch)){
                    continue;
                }
                else {
                    charMap.put(ch, 1);
                    count++;
                }
            }
            if(count > maxCount){
                maxCount = count;
                maxString = word;
            }
            else if(count == maxCount){
                if(word.compareTo(maxString) < 0){
                    maxString = word;
                }
            }
        }
        return maxString;
    }
}
