```java
import java.util.*;
import java.util.stream.*;

public class Solution {
    public Optional<String> longest(List<String> strings) {
        return strings.stream()
                .max(Comparator.comparingInt(String::length))
                .map(Optional::of);
    }
}
```
The solution uses Java 8's Stream API to find the longest string in the list. The `max` method is used to find the maximum string in the stream, and `Comparator.comparingInt(String::length)` is used to compare the strings based on their lengths. The `map` method is used to convert the maximum string to an `Optional` object, which is returned by the method. If the input list is empty, `max` returns an empty `Optional`, which is then wrapped in an `Optional` object by the `map` method. If the input list is not empty, `max` returns an `Optional` containing the longest string. If there are multiple strings of the same length, the first one in the list is returned.