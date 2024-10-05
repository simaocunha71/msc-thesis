```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> filterBySubstring(List<String> strings, String substring) {
        return strings.stream()
                      .filter(s -> s.contains(substring))
                      .collect(Collectors.toList());
    }
}
```