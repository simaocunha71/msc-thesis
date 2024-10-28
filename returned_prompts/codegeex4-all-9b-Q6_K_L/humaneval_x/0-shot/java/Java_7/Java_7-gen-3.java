```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> filterBySubstring(List<String> strings, String substring) {
        List<String> result = new ArrayList<>();
        for (String string : strings) {
            if (string.contains(substring)) {
                result.add(string);
            }
        }
        return result;
    }
}
```