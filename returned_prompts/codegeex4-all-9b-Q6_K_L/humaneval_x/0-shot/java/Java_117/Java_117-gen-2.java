Here is a Java solution that uses a regular expression to find all words in the input string and then filters out the words that have exactly n consonants:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        String[] words = s.split("\\s+");
        for (String word : words) {
            int consonants = 0;
            for (char c : word.toCharArray()) {
                if (!"aeiouAEIOU".contains(String.valueOf(c))) {
                    consonants++;
                }
            }
            if (consonants == n) {
                result.add(word);
            }
        }
        return result;
    }
}
```

In this solution, we first split the input string into an array of words using the `split` method with a regular expression that matches any whitespace character. Then, for each word, we count the number of consonants by iterating over the characters in the word and checking if they are not in the string "aeiouAEIOU". If the number of consonants is equal to n, we add the word to the result list. Finally, we return the result list.

This solution should work for any input string and any value of n, as long as n is a non-negative integer.