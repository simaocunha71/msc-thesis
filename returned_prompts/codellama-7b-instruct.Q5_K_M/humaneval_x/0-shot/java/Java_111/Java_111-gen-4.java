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
        Map<String, Integer> map = new HashMap<>();
        String[] words = test.split(" ");
        for (String word : words) {
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }
        List<String> maxKey = new ArrayList<>();
        int maxCount = 0;
        for (String key : map.keySet()) {
            if (map.get(key) > maxCount) {
                maxKey = new ArrayList<>();
                maxKey.add(key);
                maxCount = map.get(key);
            } else if (map.get(key) == maxCount) {
                maxKey.add(key);
            }
        }
        Map<String, Integer> result = new HashMap<>();
        for (String key : maxKey) {
            result.put(key, maxCount);
        }
        return result;
    }
}