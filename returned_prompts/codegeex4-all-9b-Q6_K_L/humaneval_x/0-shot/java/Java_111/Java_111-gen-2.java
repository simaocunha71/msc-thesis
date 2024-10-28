Here is a Java solution using HashMap and StringBuilder:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Map<String, Integer> histogram(String test) {
        if (test.isEmpty()) {
            return new HashMap<>();
        }
        String[] words = test.split(" ");
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        int maxCount = 0;
        for (int count : map.values()) {
            if (count > maxCount) {
                maxCount = count;
            }
        }
        Map<String, Integer> result = new HashMap<>();
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() == maxCount) {
                result.put(entry.getKey(), entry.getValue());
            }
        }
        return result;
    }
}
```

This solution first checks if the input string is empty, if so, it returns an empty HashMap. Then it splits the string into words and counts the occurrence of each word using a HashMap. It keeps track of the maximum count of words. Finally, it creates a new HashMap containing only the words that have the maximum count and returns it.