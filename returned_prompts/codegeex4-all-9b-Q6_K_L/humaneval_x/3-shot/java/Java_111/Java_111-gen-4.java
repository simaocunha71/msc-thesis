
The first and second solutions are fine, but the third one is a little bit too complex. Here is a more concise way to write it:

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
        Map<String, Integer> counter = new HashMap<>();
        for (String c : test.split(" ")) {
            counter.put(c, counter.getOrDefault(c, 0) + 1);
        }
        Map<String, Integer> result = new HashMap<>();
        int max = 0;
        for (Map.Entry<String, Integer> entry : counter.entrySet()) {
            if (entry.getValue() > max) {
                max = entry.getValue();
                result.clear();
                result.put(entry.getKey(), entry.getValue());
            } else if (entry.getValue() == max) {
                result.put(entry.getKey(), entry.getValue());
            }
        }
        return result;
    }
}

The fourth solution is fine, but it could be improved by using a for-each loop instead of a traditional for loop:

import java.util.*;
import java.lang.*;

class Solution