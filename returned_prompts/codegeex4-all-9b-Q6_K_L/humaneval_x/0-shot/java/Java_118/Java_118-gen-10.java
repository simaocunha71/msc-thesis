```java
import java.util.*;
import java.lang.*;

class Solution {
    public String getClosestVowel(String word) {
        for (int i = word.length() - 2; i > 0; i--) {
            if (isVowel(word.charAt(i)) && isConsonant(word.charAt(i - 1)) && isConsonant(word.charAt(i + 1))) {
                return String.valueOf(word.charAt(i));
            }
        }
        return "";
    }

    private boolean isVowel(char c) {
        return "AEIOUaeiou".indexOf(c) != -1;
    }

    private boolean isConsonant(char c) {
        return "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz".indexOf(c) != -1;
    }
}
```

This solution iterates over the string from the right side. For each character, it checks if it is a vowel and if the characters to its left and right are consonants. If all conditions are met, it returns the vowel character. If no such vowel is found, it returns an empty string.