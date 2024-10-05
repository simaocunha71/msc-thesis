```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> wordStrings(String s) {
        List<String> result = new ArrayList<>();
        String[] words = s.split("[,\\s]+");
        for (String word : words) {
            result.add(word);
        }
        return result;
    }
}
```