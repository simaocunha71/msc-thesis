Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<String> filterByPrefix(List<String> strings, String prefix) {
        return strings.stream()
                .filter(s -> s.startsWith(prefix))
                .collect(Collectors.toList());
    }
}
```

Explanation:
The `filterByPrefix` method takes a list of strings and a prefix as input. It uses the `stream` method to create a stream from the input list. The `filter` method is then used to filter the stream, keeping only the strings that start with the given prefix. Finally, the `collect` method is used to collect the filtered stream into a list, which is returned as the result. The `startsWith` method of the `String` class is used to check if a string starts with a given prefix. If the prefix is not specified (i.e., it is an empty string), this method returns true for any string. If the prefix is specified, this method returns true only for strings that start with the given prefix. The `filter` method applies this predicate to each string in the stream and keeps only the strings for which the predicate returns true. The `collect` method then collects the filtered strings into a list, which is returned as the result. The `filterByPrefix` method returns a new list containing only the strings that start with the given prefix. If the prefix is not specified, the method returns an empty list. If the input list is empty, the method returns an empty list. If the input list is not empty, the method returns a list containing all the strings that start with the given prefix. The `filterByPrefix` method is a simple and efficient way to filter a list of strings based on a given prefix. It is a good example of how to use the `stream` API in Java to perform filtering and collection operations.