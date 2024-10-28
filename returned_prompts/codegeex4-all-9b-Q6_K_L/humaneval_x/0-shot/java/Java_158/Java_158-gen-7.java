```java
import java.util.*;
import java.lang.*;

class Solution {
    public String findMax(List<String> words) {
        Map<String, Integer> uniqueChars = new HashMap<>();
        for (String word : words) {
            uniqueChars.put(word, uniqueChar(word));
        }
        int maxUnique = Collections.max(uniqueChars.values());
        List<String> maxWords = new ArrayList<>();
        for (String word : uniqueChars.keySet()) {
            if (uniqueChars.get(word) == maxUnique) {
                maxWords.add(word);
            }
        }
        Collections.sort(maxWords);
        return maxWords.get(0);
    }

    private int uniqueChar(String word) {
        Set<Character> unique = new HashSet<>();
        for (char c : word.toCharArray()) {
            unique.add(c);
        }
        return unique.size();
    }
}
```