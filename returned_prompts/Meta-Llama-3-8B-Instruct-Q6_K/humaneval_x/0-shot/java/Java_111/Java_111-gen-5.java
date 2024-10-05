```java
import java.util.*;

class Solution {
    public Map<String, Integer> histogram(String test) {
        if (test.isEmpty()) {
            return new HashMap<>();
        }

        Map<String, Integer> histogram = new HashMap<>();
        String[] words = test.split(" ");
        Map<String, Integer> letterCount = new HashMap<>();

        for (String word : words) {
            for (char c : word.toCharArray()) {
                letterCount.put(String.valueOf(c), letterCount.getOrDefault(String.valueOf(c), 0) + 1);
            }
        }

        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : letterCount.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
            }
        }

        for (Map.Entry<String, Integer> entry : letterCount.entrySet()) {
            if (entry.getValue() == maxCount) {
                histogram.put(entry.getKey(), entry.getValue());
            }
        }

        return histogram;
    }
}
```

This solution first splits the input string into words and then counts the occurrence of each letter in the words. It keeps track of the maximum count and then puts all the letters with the maximum count into the histogram map. If the input string is empty, it returns an empty map. The time complexity is O(n), where n is the number of words in the input string, and the space complexity is O(n), where n is the number of unique letters in the input string.