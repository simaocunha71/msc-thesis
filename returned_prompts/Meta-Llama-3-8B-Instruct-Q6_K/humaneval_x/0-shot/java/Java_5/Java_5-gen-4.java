Here is the correct code:

```java
import java.util.*;

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

This code creates a new list `result` and iterates over the input list `numbers`. For each element, it adds the element to `result` and then checks if it's not the last element in `numbers`. If it's not the last element, it adds the delimiter to `result`. The resulting list is returned. This way, the delimiter is inserted between every two consecutive elements of the input list.