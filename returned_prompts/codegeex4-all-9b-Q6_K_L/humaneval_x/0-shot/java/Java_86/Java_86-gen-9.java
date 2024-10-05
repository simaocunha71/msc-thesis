```java
import java.util.*;
import java.lang.*;

class Solution {
    public String antiShuffle(String s) {
        String[] words = s.split(" ");
        for (int i = 0; i < words.length; i++) {
            char[] chars = words[i].toCharArray();
            Arrays.sort(chars);
            words[i] = new String(chars);
        }
        return String.join(" ", words);
    }
}
```