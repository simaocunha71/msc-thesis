Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public String findMax(List<String> words) {
        String maxWord = "";
        int maxUniqueChars = 0;

        for (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }
            if (uniqueChars.size() > maxUniqueChars) {
                maxUniqueChars = uniqueChars.size();
                maxWord = word;
            } else if (uniqueChars.size() == maxUniqueChars) {
                if (word.compareTo(maxWord) < 0) {
                    maxWord = word;
                }
            }
        }
        return maxWord;
    }
}
```

In this solution, we iterate over each word in the list. For each word, we create a Set to store the unique characters. We then check if the size of the Set is greater than the current maximum unique characters. If it is, we update the maximum unique characters and the maximum word. If the size is equal to the maximum unique characters, we check if the word is lexicographically smaller than the current maximum word, and if it is, we update the maximum word. Finally, we return the maximum word.