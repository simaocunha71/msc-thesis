Here is a Java solution that uses a HashMap to store the frequency of each character in the string. It then finds the maximum frequency and returns a new HashMap with all the characters that have this frequency.

```java
import java.util.*;

class Solution {
    public Map<String, Integer> histogram(String test) {
        if (test.isEmpty()) {
            return new HashMap<>();
        }

        Map<String, Integer> histogram = new HashMap<>();
        String[] words = test.split(" ");
        for (String word : words) {
            for (char c : word.toCharArray()) {
                histogram.put(String.valueOf(c), histogram.getOrDefault(String.valueOf(c), 0) + 1);
            }
        }

        int maxFrequency = 0;
        for (Map.Entry<String, Integer> entry : histogram.entrySet()) {
            if (entry.getValue() > maxFrequency) {
                maxFrequency = entry.getValue();
            }
        }

        Map<String, Integer> result = new HashMap<>();
        for (Map.Entry<String, Integer> entry : histogram.entrySet()) {
            if (entry.getValue() == maxFrequency) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }
}
```
In this solution, we first split the input string into an array of words using the `split` method. Then, for each word, we iterate over its characters and increment their frequencies in the `histogram` map using the `put` method.

Next, we find the maximum frequency in the `histogram` map by iterating over its entries and keeping track of the maximum frequency found.

Finally, we create a new `result` map that contains all the entries from the `histogram` map with the maximum frequency. We use the `getOrDefault` method to increment the frequency of each character, and the `put` method to add the character and its frequency to the `result` map.

The solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n), where n is the number of unique characters in the input string. It works correctly even if the input string is empty, in which case it returns an empty map.