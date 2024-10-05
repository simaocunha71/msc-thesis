Here is a Java solution that uses a HashSet to store the words that contain exactly n consonants and then returns a list of these words:

```java
import java.util.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        Set<String> words = new HashSet<>();
        String[] strArray = s.split(" ");
        for (String str : strArray) {
            if (str.length() > 1) {
                int consonantCount = 0;
                for (char c : str.toLowerCase().toCharArray()) {
                    if (!Character.isLetter(c) || c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                        continue;
                    }
                    consonantCount++;
                }
                if (consonantCount == n) {
                    words.add(str);
                }
            }
        }
        result.addAll(words);
        return result;
    }
}
```

This solution first splits the input string into an array of words using the `split` method. Then, for each word, it counts the number of consonants by iterating over the characters in the word and checking if they are letters (using `Character.isLetter`) and not vowels (using `c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'`). If the consonant count matches the given number n, the word is added to the `words` set. Finally, the `result` list is filled with the words from the `words` set and returned.

Note that this solution is case-insensitive and considers words with spaces as separate words. It also ignores words with less than 2 characters. You can modify the solution to fit your specific requirements.