Here is a Java solution to the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        String[] words = s.split(" ");
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (word.length() >= n) {
                int consonantCount = 0;
                for (char c : word.toCharArray()) {
                    if (!isVowel(c)) {
                        consonantCount++;
                    }
                }
                if (consonantCount == n) {
                    result.add(word);
                }
            }
        }
        return result;
    }

    private boolean isVowel(char c) {
        c = Character.toLowerCase(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
```

This solution first splits the input string into an array of words. Then, it iterates over each word and checks if its length is at least n. If it is, it counts the number of consonants in the word and checks if this count is equal to n. If it is, the word is added to the result list. Finally, the result list is returned.