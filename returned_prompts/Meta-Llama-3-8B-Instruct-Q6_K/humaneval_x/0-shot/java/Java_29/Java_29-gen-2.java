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

*   We use the `stream()` method to convert the input list of strings into a stream.
*   We then use the `filter()` method to filter the stream, only keeping the elements that start with the given prefix. We use the `startsWith()` method to check if a string starts with the prefix.
*   Finally, we use the `collect()` method to collect the filtered elements into a new list. The `Collectors.toList()` method is used to create a list from the stream.
*   The resulting list is then returned by the `filterByPrefix()` method.