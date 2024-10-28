```java
import java.util.*;
import java.lang.*;

class Solution {
    public String antiShuffle(String s) {
        // Split the input string into words
        String[] words = s.split(" ");
        // Create a list to store the sorted words
        List<String> sortedWords = new ArrayList<>();
        // Iterate over each word
        for (String word : words) {
            // Convert the word to a char array
            char[] chars = word.toCharArray();
            // Sort the char array
            Arrays.sort(chars);
            // Convert the sorted char array back to a string
            String sortedWord = new String(chars);
            // Add the sorted word to the list
            sortedWords.add(sortedWord);
        }
        // Join the sorted words with spaces
        String result = String.join(" ", sortedWords);
        return result;
    }
}
```