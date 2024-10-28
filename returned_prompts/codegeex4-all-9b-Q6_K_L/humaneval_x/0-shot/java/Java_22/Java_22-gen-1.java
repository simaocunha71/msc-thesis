Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Filter given list of any values only for integers
    >>> filterIntergers(Arrays.asList('a', 3.14, 5))
    [5]
    >>> filterIntergers(Arrays.asList(1, 2, 3, "abc", Map.of(), List.of()))
    [1, 2, 3]
     */
    public List<Integer> filterIntergers(List<Object> values) {
        List<Integer> result = new ArrayList<>();
        for(Object value : values) {
            if(value instanceof Integer) {
                result.add((Integer)value);
            }
        }
        return result;
    }
}
```
This solution is using the `instanceof` operator to check if an object is an instance of a specific class. If the object is an instance of `Integer`, it is added to the result list.