```java
import java.util.*;

public class Solution {
    public List<String> filterBySubstring(List<String> strings, String substring) {
        return strings.stream()
                .filter(s -> s.contains(substring))
                .collect(Collectors.toList());
    }
}
```

Explanation:
This problem is asking to create a method that filters a list of strings to include only those that contain a given substring. The method should return a new list with the filtered strings.

In the provided code, we use Java 8's Stream API to solve this problem. The `filter` method is used to filter the strings based on whether they contain the given substring. The `contains` method checks if a string contains a certain substring. If a string contains the substring, it is included in the resulting list. The `collect` method is used to collect the filtered strings into a new list.

The method can be tested with sample inputs to verify its correctness. For example, `filterBySubstring(Arrays.asList("abc", "bacd", "cde", "array"), "a")` should return `["abc", "bacd", "array"]`. If the input list is empty, the method will return an empty list. This is demonstrated in the unit test `filterBySubstring(List.of(), "a")` which returns an empty list.