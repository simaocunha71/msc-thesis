Here is a Java solution that uses a regular expression to split the string into words, and then checks each word to see if it contains exactly n consonants. The words that meet this condition are added to a list, which is then returned.

```java
import java.util.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");
        for (String word : words) {
            int consonantCount = 0;
            for (char c : word.toCharArray()) {
                if (!Character.isLetter(c)) continue;
                if (Character.toLowerCase(c) != 'a' && Character.toLowerCase(c) != 'e' && Character.toLowerCase(c) != 'i' && Character.toLowerCase(c) != 'o' && Character.toLowerCase(c) != 'u') {
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

This solution works by iterating over each word in the input string, and for each word, it counts the number of consonants. It does this by iterating over each character in the word, and for each character, it checks if it is a letter (using `Character.isLetter(c)`). If it is a letter, it checks if it is a vowel (using `Character.toLowerCase(c) != 'a' && ...`). If it is not a vowel, it increments the consonant count. Finally, if the consonant count is equal to n, it adds the word to the result list.

The regular expression `"\\s+"` is used to split the input string into words. This regular expression matches one or more whitespace characters, so it effectively splits the string into words separated by spaces. The `split` method returns an array of strings, where each string is a word from the input string.

The `Character.toLowerCase(c) != 'a' && ...` check is used to determine if a character is a consonant. This check is not perfect, as it does not account for characters that are not letters (such as punctuation or digits). However, it is sufficient for the purpose of this problem, since we are only considering letters. If we wanted to handle non-letter characters, we would need a more sophisticated check.