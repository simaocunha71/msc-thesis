```java
import java.util.*;
import java.lang.*;

class Solution {
    public String findMax(List<String> words) {
        String max = "";
        int maxUnique = 0;
        for (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }
            if (uniqueChars.size() > maxUnique || (uniqueChars.size() == maxUnique && word.compareTo(max) < 0)) {
                max = word;
                maxUnique = uniqueChars.size();
            }
        }
        return max;
    }
}
```