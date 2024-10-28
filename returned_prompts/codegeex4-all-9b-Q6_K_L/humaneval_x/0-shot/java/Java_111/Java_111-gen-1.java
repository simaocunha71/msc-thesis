Here is the solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> histogram = new HashMap<>();
        Map<String, Integer> countMap = new HashMap<>();
        String[] words = test.split(" ");

        for (String word : words) {
            countMap.put(word, countMap.getOrDefault(word, 0) + 1);
        }

        int max = 0;
        for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() > max) {
                max = entry.getValue();
                histogram.clear();
                histogram.put(entry.getKey(), entry.getValue());
            } else if (entry.getValue() == max) {
                histogram.put(entry.getKey(), entry.getValue());
            }
        }

        return histogram;
    }
}
```

In this solution, we first split the input string into words. Then, we count the occurrence of each word and store the count in a map called `countMap`. After that, we iterate through the `countMap` to find the maximum count and store the corresponding words in the `histogram` map. If we encounter a word with the same count as the maximum, we add it to the `histogram` map. Finally, we return the `histogram` map.