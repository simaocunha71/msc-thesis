Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
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
Here's an explanation of the solution:

1. First, we split the input string `s` into an array of words using the `split()` method with a space character as the delimiter.
2. We iterate through each word in the array and count the number of consonants in the word using a nested loop. We only consider letters and ignore spaces, punctuation, and uppercase letters.
3. We check if the consonant count of the current word is equal to the input `n`. If it is, we add the word to the result list.
4. Finally, we return the result list.

Note that we use the `Character.isLetter()` method to check if a character is a letter, and `Character.isUpperCase()` to check if a letter is uppercase. We also use the `toCharArray()` method to convert the word to an array of characters, and the `continue` statement to skip non-letter characters and uppercase letters.