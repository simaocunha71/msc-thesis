```java
import java.util.*;
import java.lang.*;

class Solution {
    public String antiShuffle(String s) {
        List<String> words = Arrays.asList(s.split(" "));
        List<String> sortedWords = new ArrayList<>();
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            sortedWords.add(new String(chars));
        }
        return String.join(" ", sortedWords);
    }
}
```