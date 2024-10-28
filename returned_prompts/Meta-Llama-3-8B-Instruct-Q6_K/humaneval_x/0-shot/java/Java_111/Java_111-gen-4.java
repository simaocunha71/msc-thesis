```java
import java.util.*;

public class Solution {
    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> map = new HashMap<>();
        if (test.isEmpty()) {
            return map;
        }
        String[] words = test.split(" ");
        for (String word : words) {
            if (!map.containsKey(word)) {
                map.put(word, 1);
            } else {
                map.put(word, map.get(word) + 1);
            }
        }
        Map<String, Integer> maxMap = new HashMap<>();
        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                maxMap.clear();
                maxMap.put(entry.getKey(), entry.getValue());
            } else if (entry.getValue() == maxCount) {
                maxMap.put(entry.getKey(), entry.getValue());
            }
        }
        return maxMap;
    }
}
```


The code takes a string as input and returns a map where the keys are the letters in the string and the values are the counts of each letter.

The code first splits the input string into an array of words using the `split` method with a space character as the delimiter.

Then it iterates over the array of words and for each word, it checks if the word is already present in the map. If it is not present, it adds the word to the map with a count of 1. If it is already present, it increments the count by 1.

After that, it iterates over the map and finds the maximum count. It then creates a new map with the letters that have the maximum count.

Finally, it returns the new map.

The time complexity of this code is O(n), where n is the number of words in the input string. The space complexity is also O(n), as in the worst case, the map will contain all the words in the input string. 