Here is a solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        // Split the string into words
        String[] words = s.split(" ");
        
        // Create a list to store the selected words
        List<String> selectedWords = new ArrayList<>();
        
        // Iterate over the words
        for (String word : words) {
            // Count the number of consonants in the word
            int consonants = 0;
            for (char c : word.toCharArray()) {
                // Check if the character is a consonant
                if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U') {
                    consonants++;
                }
            }
            
            // If the number of consonants is equal to n, add the word to the selected words list
            if (consonants == n) {
                selectedWords.add(word);
            }
        }
        
        // Return the selected words list
        return selectedWords;
    }
}
```

This solution first splits the input string into words using the `split` method. Then, it iterates over the words and counts the number of consonants in each word. If the number of consonants is equal to the given number `n`, the word is added to the selected words list. Finally, the selected words list is returned.