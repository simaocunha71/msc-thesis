```java
import java.util.*;
import java.lang.*;

class Solution {
    public String antiShuffle(String s) {
        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();

        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            sb.append(new String(chars)).append(" ");
        }

        return sb.toString().trim();
    }
}
```