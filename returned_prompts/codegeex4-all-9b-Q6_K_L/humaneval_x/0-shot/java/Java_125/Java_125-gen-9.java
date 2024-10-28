```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object splitWords(String txt) {
        if (txt == null || txt.isEmpty()) {
            return new ArrayList<>();
        }
        List<String> words = new ArrayList<>();
        StringBuilder currentWord = new StringBuilder();
        for (char c : txt.toCharArray()) {
            if (Character.isWhitespace(c)) {
                if (currentWord.length() > 0) {
                    words.add(currentWord.toString());
                    currentWord.setLength(0);
                }
            } else if (c == ',') {
                if (currentWord.length() > 0) {
                    words.add(currentWord.toString());
                    currentWord.setLength(0);
                }
                words.add(",");
            } else {
                currentWord.append(c);
            }
        }
        if (currentWord.length() > 0) {
            words.add(currentWord.toString());
        }
        if (words.isEmpty()) {
            int oddCount = 0;
            for (char c : txt.toCharArray()) {
                if (Character.isLowerCase(c) && (c - 'a') % 2 == 1) {
                    oddCount++;
                }
            }
            return oddCount;
        } else {
            return words;
        }
    }
}
```

This solution works by iterating through the characters of the input string and checking for whitespace or comma characters. If a whitespace or comma is found, the current word is added to the list of words and a new word is started. If a non-whitespace, non-comma character is found, it is added to the current word. After iterating through all characters, if there is still a current word, it is added to the list of words. If the list of words is empty, it means that there were no words or commas in the input string, so the number of lower-case letters with odd order in the alphabet is returned. Otherwise, the list of words is returned.