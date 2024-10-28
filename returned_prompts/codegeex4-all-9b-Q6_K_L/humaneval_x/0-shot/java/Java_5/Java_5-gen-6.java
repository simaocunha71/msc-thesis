Here's the Java implementation:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            if (i < numbers.size() - 1) {
                result.add(delimiter);
            }
        }
        return result;
    }
}
```

The `intersperse` method takes a list of integers and an integer delimiter as input. It creates a new list, `result`, and iterates over the input list. For each element in the input list, it adds the element to the `result` list and, if it's not the last element in the input list, adds the delimiter to the `result` list as well.

This method should return a new list where the delimiter is inserted between every two consecutive elements of the input list.