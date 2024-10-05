Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> histogram = new HashMap<>();
        String[] words = test.split(" ");
        for (String word : words) {
            histogram.put(word, histogram.getOrDefault(word, 0) + 1);
        }
        
        Map<String, Integer> maxHistogram = new HashMap<>();
        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : histogram.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                maxHistogram.clear();
                maxHistogram.put(entry.getKey(), entry.getValue());
            } else if (entry.getValue() == maxCount) {
                maxHistogram.put(entry.getKey(), entry.getValue());
            }
        }
        return maxHistogram;
    }
}
```

The `histogram` method splits the input string into words and counts the occurrences of each word using a `HashMap`. It then iterates over the entries of the `histogram` map and keeps track of the maximum count and the corresponding words in the `maxHistogram` map. Finally, it returns the `maxHistogram` map.