Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");
        for (String word : words) {
            int consonantCount = 0;
            for (char c : word.toCharArray()) {
                if (!Character.isLetter(c) || Character.isUpperCase(c)) {
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

This solution uses a simple loop to iterate over each word in the input string. For each word, it counts the number of consonants by iterating over each character in the word and checking if the character is a letter (ignoring spaces and uppercase letters) and if it is not a vowel (ignoring 'a', 'e', 'i', 'o', 'u'). If the word contains exactly `n` consonants, it adds the word to the result list. Finally, it returns the result list.

The time complexity of this solution is O(n), where n is the number of words in the input string, because it iterates over each word once. The space complexity is O(m), where m is the total number of characters in the input string, because it stores the result list.