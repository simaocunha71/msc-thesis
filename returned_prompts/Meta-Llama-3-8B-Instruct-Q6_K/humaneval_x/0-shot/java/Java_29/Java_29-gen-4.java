Here is the correct code:

```java
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public List<String> filterByPrefix(List<String> strings, String prefix) {
        return strings.stream()
                .filter(s -> s.startsWith(prefix))
                .collect(Collectors.toList());
    }
}
```

This code uses Java 8's Stream API to filter the input list of strings. It uses the `stream()` method to create a stream from the list, then the `filter()` method to filter out the strings that don't start with the given prefix. Finally, it uses the `collect()` method to collect the filtered strings into a new list. The `startsWith()` method is used to check if a string starts with a given prefix.