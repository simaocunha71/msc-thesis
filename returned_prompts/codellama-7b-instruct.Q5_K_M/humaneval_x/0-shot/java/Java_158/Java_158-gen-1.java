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
        for (String word : words) {
            for (char ch : word.toCharArray()) {
                if (map.containsKey(ch))
                    map.put(ch, map.get(ch) + 1);
                else
                    map.put(ch, 1);
            }
        }
        String ans = "";
        int max = 0;
        for (String word : words) {
            int cnt = 0;
            for (char ch : word.toCharArray()) {
                if (map.get(ch) != null)
                    cnt += map.get(ch);
            }
            if (cnt > max) {
                max = cnt;
                ans = word;
            } else if (cnt == max && ans.compareTo(word) > 0)
                ans = word;
        }
        return ans;
    }
}
