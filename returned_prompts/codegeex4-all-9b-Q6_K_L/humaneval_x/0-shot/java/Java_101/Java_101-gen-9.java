```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> wordStrings(String s) {
        if (s == null || s.isEmpty()) {
            return new ArrayList<String>();
        }
        String[] words = s.split("[,\\s]+");
        return Arrays.asList(words);
    }
}
```