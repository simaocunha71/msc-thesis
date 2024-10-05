```java
import java.util.*;
import java.lang.*;

class Solution {
    public String getClosestVowel(String word) {
        String vowels = "AEIOUaeiou";
        for (int i = word.length() - 1; i > 0; i--) {
            char c = word.charAt(i);
            if (vowels.indexOf(c) >= 0) {
                if (vowels.indexOf(word.charAt(i - 1)) < 0 && vowels.indexOf(word.charAt(i + 1)) < 0) {
                    return String.valueOf(c);
                }
            }
        }
        return "";
    }
}
```
