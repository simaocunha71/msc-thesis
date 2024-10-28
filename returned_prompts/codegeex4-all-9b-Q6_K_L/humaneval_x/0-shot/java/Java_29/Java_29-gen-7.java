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

Explanation:
- The `filterByPrefix` method takes a list of strings and a prefix as input.
- It uses Java 8 streams to filter the list.
- The `filter` method is used to keep only the strings that start with the given prefix.
- The `collect` method is used to convert the stream back to a list.
- Finally, the filtered list is returned.