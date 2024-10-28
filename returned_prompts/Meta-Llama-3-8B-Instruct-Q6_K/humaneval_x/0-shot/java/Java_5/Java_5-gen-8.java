Here is the Java solution for the problem:

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

This solution iterates over the input list `numbers` and adds each element to the `result` list. If the current index `i` is less than the size of the list minus one, it means we are not at the last element, so we add the `delimiter` to the `result` list as well. Finally, we return the `result` list.