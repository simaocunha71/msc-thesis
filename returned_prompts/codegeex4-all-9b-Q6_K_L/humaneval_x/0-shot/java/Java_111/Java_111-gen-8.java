Here is a possible solution in Java:

```java
import java.util.*;

class Solution {
    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> map = new HashMap<>();
        String[] words = test.split(" ");
        int maxCount = 0;

        for (String word : words) {
            if (map.containsKey(word)) {
                int count = map.get(word) + 1;
                map.put(word, count);
                maxCount = Math.max(maxCount, count);
            } else {
                map.put(word, 1);
            }
        }

        Map<String, Integer> result = new HashMap<>();
        for (String key : map.keySet()) {
            if (map.get(key) == maxCount) {
                result.put(key, maxCount);
            }
        }

        return result;
    }
}
```

This code first splits the input string into an array of words. Then, it counts the occurrence of each word and stores the counts in a HashMap. After that, it finds the maximum count. Finally, it creates a new HashMap and adds only the words that have the maximum count to it. This new HashMap is then returned as the result.

Note: This code assumes that the input string is well-formed and does not contain any special characters.