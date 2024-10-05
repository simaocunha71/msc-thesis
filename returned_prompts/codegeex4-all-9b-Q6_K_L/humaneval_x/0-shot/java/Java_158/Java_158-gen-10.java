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
            if (uniqueChars.size() > maxUniqueChars || (uniqueChars.size() == maxUniqueChars && word.compareTo(maxWord) < 0)) {
                maxUniqueChars = uniqueChars.size();
                maxWord = word;
            }
        }
        return maxWord;
    }
}
```