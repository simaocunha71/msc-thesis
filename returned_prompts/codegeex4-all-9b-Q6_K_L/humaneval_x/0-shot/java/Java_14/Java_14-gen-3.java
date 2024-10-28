```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> allPrefixes(String string) {
        List<String> prefixes = new ArrayList<>();
        for (int i = 1; i <= string.length(); i++) {
            prefixes.add(string.substring(0, i));
        }
        return prefixes;
    }
}
```