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
        for (int i = 0; i < words.length; i++) {
            if (map.containsKey(words[i])) {
                map.put(words[i], map.get(words[i]) + 1);
            } else {
                map.put(words[i], 1);
            }
        }
        Map<String, Integer> finalMap = new HashMap<>();
        int max = 0;
        for (String key : map.keySet()) {
            if (map.get(key) > max) {
                max = map.get(key);
            }
        }
        for (String key : map.keySet()) {
            if (map.get(key) == max) {
                finalMap.put(key, map.get(key));
            }
        }
        return finalMap;
    }
}