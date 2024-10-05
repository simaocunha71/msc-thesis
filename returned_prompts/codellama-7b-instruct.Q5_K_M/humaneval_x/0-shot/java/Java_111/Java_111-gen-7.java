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

        Map<String, Integer> result = new HashMap<String, Integer>();

        // Write your code here
        String[] words = test.split(" ");

        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if (!result.containsKey(word)) {
                result.put(word, 1);
            } else {
                int count = result.get(word);
                count++;
                result.put(word, count);
            }
        }

        return result;
    }
}
