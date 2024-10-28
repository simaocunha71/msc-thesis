```java
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<String> filterByPrefix(List<String> strings, String prefix) {
        return strings.stream()
                      .filter(s -> s.startsWith(prefix))
                      .collect(Collectors.toList());
    }
}
```
