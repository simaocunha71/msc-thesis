Here is a Java solution that uses Java 8's Stream API to filter the list and keep only the integers:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> filterIntergers(List<Object> values) {
        return values.stream()
                .filter(value -> value instanceof Integer)
                .map(value -> (Integer) value)
                .collect(Collectors.toList());
    }
}
```

In this solution, we use the `stream()` method to convert the list to a stream. Then, we use the `filter()` method to filter out the elements that are not instances of `Integer`. The `map()` method is used to convert the `Integer` objects to `Integer` objects (since the `filter()` method returns a stream of `Object` instances). Finally, we use the `collect()` method to collect the filtered and mapped stream into a list. The resulting list contains only the integers from the original list.