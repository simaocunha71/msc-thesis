Here is a simple implementation of the problem:

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

This solution iterates over the input list `numbers` and adds each element to the result list. If the current index is less than the last index of the list, it adds the delimiter to the result list. Finally, it returns the result list. This solution works for any input list and delimiter. For example, if the input list is `[1, 2, 3]` and the delimiter is `4`, the output will be `[1, 4, 2, 4, 3]`. If the input list is empty, the output will be an empty list.