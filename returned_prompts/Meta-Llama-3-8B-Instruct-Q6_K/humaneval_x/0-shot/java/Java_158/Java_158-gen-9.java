Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public String findMax(List<String> words) {
        String maxWord = "";
        int maxCount = 0;
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > maxCount) {
                maxCount = set.size();
                maxWord = word;
            } else if (set.size() == maxCount) {
                maxWord = maxWord.compareTo(word) < 0 ? maxWord : word;
            }
        }
        return maxWord;
    }
}
```
The function iterates over each word in the list. For each word, it creates a set of unique characters using a HashSet. Then, it checks if the size of the set is greater than the current maximum count. If it is, it updates the maximum count and the maximum word. If the size of the set is equal to the maximum count, it compares the current word with the maximum word and updates the maximum word if it is smaller in lexicographical order.

The function returns the maximum word. If no word has unique characters, it returns an empty string.