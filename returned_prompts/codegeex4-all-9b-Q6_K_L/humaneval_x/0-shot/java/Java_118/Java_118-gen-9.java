```java
import java.util.*;
import java.lang.*;

class Solution {
    public String getClosestVowel(String word) {
        String vowels = "aeiouAEIOU";
        for (int i = word.length() - 1; i > 0; i--) {
            char c = word.charAt(i);
            if (vowels.indexOf(c) != -1 && !vowels.contains(word.charAt(i - 1) + "") && !vowels.contains(word.charAt(i + 1) + "")) {
                return c + "";
            }
        }
        return "";
    }
}
```
This solution works by iterating through the word from right to left. For each character, it checks if it is a vowel and if the characters before and after it are not vowels. If it is a vowel and the characters before and after it are not vowels, it returns the vowel. If it doesn't find any vowel that meets the above condition, it returns an empty string.