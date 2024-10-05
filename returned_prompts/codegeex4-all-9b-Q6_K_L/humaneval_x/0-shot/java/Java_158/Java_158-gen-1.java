Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String findMax(List<String> words) {
        Map<String, Integer> wordCharCount = new HashMap<>();
        for (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }
            wordCharCount.put(word, uniqueChars.size());
        }

        String maxWord = "";
        int maxUniqueChars = 0;
        for (Map.Entry<String, Integer> entry : wordCharCount.entrySet()) {
            if (entry.getValue() > maxUniqueChars || (entry.getValue() == maxUniqueChars && entry.getKey().compareTo(maxWord) < 0)) {
                maxUniqueChars = entry.getValue();
                maxWord = entry.getKey();
            }
        }

        return maxWord;
    }
}
```

This solution first creates a `HashMap` to store the count of unique characters for each word. It then iterates through the `HashMap` to find the word with maximum number of unique characters. If multiple words have the same number of unique characters, it returns the one which comes first in lexicographical order.