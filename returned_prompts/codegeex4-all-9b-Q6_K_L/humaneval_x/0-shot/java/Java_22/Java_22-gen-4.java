```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Filter given list of any values only for integers
    >>> filter_integers(Arrays.asList('a', 3.14, 5))
    [5]
    >>> filter_integers(Arrays.asList(1, 2, 3, "abc", Map.of(), List.of()))
    [1, 2, 3]
     */
    public List<Integer> filterIntegers(List<Object> values) {
        List<Integer> result = new ArrayList<>();
        for (Object obj : values) {
            if (obj instanceof Integer) {
                result.add((Integer) obj);
            }
        }
        return result;
    }
}
```