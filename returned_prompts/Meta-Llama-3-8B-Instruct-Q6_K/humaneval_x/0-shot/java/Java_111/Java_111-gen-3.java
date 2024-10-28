    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> result = new HashMap<>();
        if (test.isEmpty()) {
            return result;
        }

        String[] words = test.split(" ");
        int maxCount = 0;
        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (result.containsKey(String.valueOf(c))) {
                    count = result.get(String.valueOf(c));
                }
                result.put(String.valueOf(c), count + 1);
            }
        }

        maxCount = Collections.max(result.values());
        Map<String, Integer> maxCountResult = new HashMap<>();
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() == maxCount) {
                maxCountResult.put(entry.getKey(), entry.getValue());
            }
        }

        return maxCountResult;
    }   


This solution first splits the input string into individual characters, then counts the occurrence of each character. It then finds the maximum count and creates a new map containing only the characters with the maximum count. The function returns this new map.

The time complexity of this solution is O(n), where n is the length of the input string. The space complexity is also O(n), as in the worst case, all characters in the input string are unique and therefore need to be stored in the map.   


The histogram function takes a string as input and returns a map where the keys are the unique characters in the string and the values are the counts of each character. If there are multiple characters with the same maximum count, the function returns all of them. If the input string is empty, the function returns an empty map.   


The function first splits the input string into individual characters using the split function. Then, it iterates over the characters and counts their occurrences using a HashMap. The maximum count is found using the max function from the Collections class. Finally, the function creates a new map containing only the characters with the maximum count and returns it.   


The time complexity of this function is O(n), where n is the length of the input string. The space complexity is also O(n), as in the worst case, all characters in the input string are unique and therefore need to be stored in the map.   


Here is the code for the histogram function:

```java
import java.util.*;

public class Solution {
    public Map<String, Integer> histogram(String test) {
        Map<String,