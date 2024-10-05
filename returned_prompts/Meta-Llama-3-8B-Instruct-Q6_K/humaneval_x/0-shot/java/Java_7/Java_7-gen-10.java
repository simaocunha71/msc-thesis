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
This Java solution uses the Stream API to filter the input list of strings. The `filter` method is used to select only the strings that contain the given substring. The `contains` method is used to check if a string contains a certain substring. The `collect` method is then used to collect the filtered strings into a new list. This solution is concise, efficient, and easy to understand. It also works for empty input lists and lists with no strings containing the given substring.