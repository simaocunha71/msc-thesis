Here is the Java code that filters a list of strings by prefix:
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
This solution uses Java 8's Stream API to filter the list of strings. The `stream()` method converts the list to a stream, `filter(s -> s.startsWith(prefix))` applies a predicate to each string, and `collect(Collectors.toList())` collects the filtered strings into a new list.

Note that this solution uses the `startsWith()` method from the `String` class, which returns `true` if the string starts with the given prefix. If you want to make the prefix case-insensitive, you can use the `toLowerCase()` or `toUpperCase()` method to normalize the prefix and the strings before comparing them. For example:
```java
return strings.stream()
        .filter(s -> s.toLowerCase().startsWith(prefix.toLowerCase()))
        .collect(Collectors.toList());
```
This way, the filter will match strings that start with the prefix regardless of the case.