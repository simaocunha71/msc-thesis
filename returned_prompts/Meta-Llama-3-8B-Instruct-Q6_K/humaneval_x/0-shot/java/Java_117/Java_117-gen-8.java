Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");
        for (String word : words) {
            int consonantCount = 0;
            for (char c : word.toLowerCase().toCharArray()) {
                if (!Character.isLetter(c)) {
                    continue;
                }
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                    consonantCount++;
                }
            }
            if (consonantCount == n) {
                result.add(word);
            }
        }
        return result;
    }
}
```

In this solution, we split the input string into words and then iterate over each word. We count the number of consonants in each word and add it to the result list if the count matches the given number. The `Character.isLetter(c)` method is used to check if the character is a letter, and the `c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u'` condition is used to check if the character is a consonant. The `toLowerCase()` method is used to convert the word to lowercase to make the comparison case-insensitive. Finally, the result list is returned.