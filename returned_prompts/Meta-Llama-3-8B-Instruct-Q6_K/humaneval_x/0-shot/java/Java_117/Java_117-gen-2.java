```java
import java.util.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");
        for (String word : words) {
            int consonantCount = 0;
            for (char c : word.toCharArray()) {
                if (!Character.isLetter(c)) {
                    continue;
                }
                if (!Character.isLowerCase(c) && !Character.isUpperCase(c)) {
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

Explanation:
This problem can be solved by first splitting the input string into individual words. Then, for each word, we iterate over each character in the word and count the number of consonants. A consonant is defined as any letter that is not a vowel (i.e., 'a', 'e', 'i', 'o', 'u'). If the count of consonants matches the given number n, we add the word to the result list.

Here is a step-by-step breakdown of the solution:

1. Split the input string s into individual words using the `split` method with a regular expression that matches one or more whitespace characters (`\\s+`).
2. Initialize an empty list `result` to store the words that contain exactly n consonants.
3. Iterate over each word in the array of words.
4. Initialize a variable `consonantCount` to 0 to count the number of consonants in the word.
5. Iterate over each character in the word using a `for` loop.
6. Check if the character is a letter using the `Character.isLetter` method. If it is not a letter, skip to the next iteration.
7. Check if the character is not a lowercase or uppercase letter using the `Character.isLowerCase` and `Character.isUpperCase` methods. If it is not a letter, skip to the next iteration.
8. Check if the character is not a vowel (i.e., 'a', 'e', 'i', 'o', 'u') using a conditional statement. If it is a vowel, skip to the next iteration.
9. If the character is a conson