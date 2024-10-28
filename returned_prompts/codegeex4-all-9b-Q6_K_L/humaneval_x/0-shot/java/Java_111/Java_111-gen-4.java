import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.

    Example:
    histogram("a b c") == {"a": 1, "b": 1, "c": 1}
    histogram("a b b a") == {"a": 2, "b": 2}
    histogram("a b c a b") == {"a": 2, "b": 2}
    histogram("b b b b a") == {"b": 4}
    histogram("") == {}
     */
    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> result = new HashMap<>();
        if (test == null || test.length() == 0) {
            return result;
        }
        String[] words = test.split(" ");
        Map<String, Integer> wordCount = new HashMap<>();
        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }
        int max = 0;
        for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {
            if (entry.getValue() > max) {
                max = entry.getValue();
            }
        }
        for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {
            if (entry.getValue() == max) {
                result.put(entry.getKey(), entry.getValue());
            }
        }
        return result;
    }
}