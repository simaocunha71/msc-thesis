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
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        String maxWord = "";
        int maxUniqueChar = 0;
        for (String word : words) {
            map.clear();
            int uniqueChar = 0;
            for (char c : word.toCharArray()) {
                if (map.containsKey(c)) continue;
                else map.put(c, 1);
                uniqueChar++;
            }
            if (uniqueChar > maxUniqueChar) {
                maxUniqueChar = uniqueChar;
                maxWord = word;
            } else if (uniqueChar == maxUniqueChar) {
                if (maxWord.compareTo(word) > 0) {
                    maxWord = word;
                }
            }
        }
        return maxWord;
    }

    public static void main(String[] args) {
        List<String> words = new ArrayList<String>();
        words.add("name");
        words.add("of");
        words.add("string");
        words.add("enam");
        words.add("game");
        words.add("aaaaaaa");
        words.add("bb");
        words.add("cc");
        Solution s = new Solution();
        String result = s.findMax(words);
        System.out.println(result);
    }
}

