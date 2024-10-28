Here is a Java solution using HashMap:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Map<String, Integer> histogram(String test) {
        // Split the string into an array of words
        String[] words = test.split(" ");
        
        // Create a HashMap to store the words and their counts
        Map<String, Integer> map = new HashMap<String, Integer>();
        
        // Loop through each word in the array
        for (String word : words) {
            // If the word is already in the map, increment its count
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            // Otherwise, add the word to the map with a count of 1
            } else {
                map.put(word, 1);
            }
        }
        
        // Create a list to store the words with the highest count
        List<String> maxWords = new ArrayList<String>();
        
        // Set the initial maximum count to 0
        int maxCount = 0;
        
        // Loop through each word in the map
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            // If the word's count is higher than the current maximum, update the maximum
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                maxWords.clear();
                maxWords.add(entry.getKey());
            // If the word's count is equal to the current maximum, add the word to the list
            } else if (entry.getValue() == maxCount) {
                maxWords.add(entry.getKey());
            }
        }
        
        // Create a new HashMap to store the words with the highest count and their counts
        Map<String, Integer> result = new HashMap<String, Integer>();
        
        // Loop through each word in the list
        for (String word : maxWords) {
            // Add the word and its count to the result map
            result.put(word, maxCount);
        }
        
        // Return the result map
        return result;
    }
}
```

This solution splits the input string into an array of words, then creates a HashMap to store the words and their counts. It loops through each word in the array, and if the word is already in the map, it increments its count. If the word is not in the map, it adds the word with a count of 1. It then creates a list to store the words with the highest count,