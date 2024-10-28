Here is a Java solution to the problem:

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

This solution works by first splitting the input string into individual words. Then, for each word, it counts the number of consonants. A consonant is defined as any letter that is not a vowel (a, e, i, o, u). If the count of consonants matches the given number n, the word is added to the result list.

Note that the solution converts the word to lowercase before counting the consonants to make the solution case-insensitive. It also uses a continue statement to skip non-letter characters in the word.

The solution returns the result list at the end. If the input string is empty, the function will return an empty list. Otherwise, it will return a list of words that contain exactly n consonants.