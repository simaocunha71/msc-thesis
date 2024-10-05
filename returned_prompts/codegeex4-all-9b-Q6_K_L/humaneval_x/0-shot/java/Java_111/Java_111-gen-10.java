Here is the Java code that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> histogram = new HashMap<>();
        if (test.isEmpty()) {
            return histogram;
        }
        String[] words = test.split(" ");
        for (String word : words) {
            histogram.put(word, histogram.getOrDefault(word, 0) + 1);
        }
        return histogram;
    }
}
```
This code first checks if the input string is empty, if so it returns an empty histogram. Then it splits the string into words and for each word it increments its count in the histogram map. The `getOrDefault` method is used to get the count of a word from the map, if the word is not in the map, it returns 0.