Here is the solution in Java:

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

This solution uses a simple loop to iterate over the input list `numbers`. For each element, it adds the element to the result list and then adds the delimiter if it's not the last element in the list. The result list is then returned.

For example, if you call `intersperse(Arrays.asList(1, 2, 3), 4)`, the method will return `[1, 4, 2, 4, 3]`, which is the desired output. If you call `intersperse(new ArrayList<>(), 4)`, the method will return an empty list `[]`, which is also the desired output.