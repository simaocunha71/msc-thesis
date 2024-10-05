```java
import java.util.*;
import java.lang.*;

class Solution {
    public String getClosestVowel(String word) {
        // Vowels in the beginning and ending doesn't count.
        if (word.length() <= 2) return "";
        // Remove the first and last characters.
        word = word.substring(1, word.length() - 1);
        for (int i = word.length() - 1; i >= 0; i--) {
            char c = word.charAt(i);
            // Check if the current character is a vowel.
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                // Check if the characters before and after the current character are consonants.
                if (isConsonant(word.charAt(i - 1)) && isConsonant(word.charAt(i + 1))) {
                    return String.valueOf(c);
                }
            }
        }
        return "";
    }

    private boolean isConsonant(char c) {
        return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' &&
               c != 'A' && c != 'E' && c != 'I' && c != 'O' && c != 'U';
    }
}
```

This solution works by first removing the first and last characters of the given word. Then, it iterates through the word from right to left, checking if the current character is a vowel and if the characters before and after it are consonants. If both conditions are met, it returns the current character. If no such character is found, it returns an empty string.