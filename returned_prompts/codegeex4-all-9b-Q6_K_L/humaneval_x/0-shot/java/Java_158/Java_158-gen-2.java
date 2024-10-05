```java
import java.util.*;
import java.lang.*;

class Solution {
    public String findMax(List<String> words) {
        if (words == null || words.isEmpty()) {
            return "";
        }
        
        String maxWord = words.get(0);
        int maxUniqueChars = countUniqueChars(maxWord);
        
        for (int i = 1; i < words.size(); i++) {
            String word = words.get(i);
            int uniqueChars = countUniqueChars(word);
            
            if (uniqueChars > maxUniqueChars) {
                maxWord = word;
                maxUniqueChars = uniqueChars;
            } else if (uniqueChars == maxUniqueChars) {
                maxWord = maxWord.compareTo(word) < 0 ? maxWord : word;
            }
        }
        
        return maxWord;
    }
    
    private int countUniqueChars(String word) {
        Set<Character> uniqueChars = new HashSet<>();
        
        for (char c : word.toCharArray()) {
            uniqueChars.add(c);
        }
        
        return uniqueChars.size();
    }
}
```