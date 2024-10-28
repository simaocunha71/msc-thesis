import java.util.*;
import java.lang.*;

class Solution {
    public Map<String, Integer> histogram(String test) {

        if (test == null || test.isEmpty()) {
            return new HashMap<>();
        }

        String[] words = test.split(" ");
        Map<String, Integer> histogram = new HashMap<>();
        int maxCount = 0;

        for (String word : words) {
            if (histogram.containsKey(word)) {
                int count = histogram.get(word) + 1;
                histogram.put(word, count);
                maxCount = Math.max(maxCount, count);
            } else {
                histogram.put(word, 1);
            }
        }

        Map<String, Integer> result = new HashMap<>();
        for (Map.Entry<String, Integer> entry : histogram.entrySet()) {
            if (entry.getValue() == maxCount) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }
}