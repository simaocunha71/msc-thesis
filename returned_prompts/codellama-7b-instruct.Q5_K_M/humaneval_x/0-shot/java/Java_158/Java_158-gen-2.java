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
        // Write your code here
        // If the list is empty or contains only one element, return the only element
        if (words.size() <= 1)
            return words.size() == 1 ? words.get(0) : "";

        // Create a HashMap to store the frequency of each character
        Map<Character, Integer> map = new HashMap<>();

        // Initialize the maximum frequency of any character
        int maxFreq = 0;
        String word = "";

        for (String w : words) {
            map.clear();
            int freq = 0;

            for (char c : w.toCharArray()) {
                // If the character is already present in the HashMap, increment its frequency
                if (map.containsKey(c))
                    freq = map.get(c) + 1;
                else
                    freq = 1;

                // Update the maximum frequency
                if (freq > maxFreq) {
                    maxFreq = freq;
                    word = w;
                }

                // Update the frequency in the HashMap
                map.put(c, freq);
            }
        }

        return word;
    }
}
