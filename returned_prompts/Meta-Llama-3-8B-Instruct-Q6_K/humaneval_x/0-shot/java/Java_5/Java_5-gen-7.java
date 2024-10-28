Here is the solution using Java:

```java
import java.util.*;

class Solution {
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        List<Integer> result = new ArrayList<>();
        for (Integer num : numbers) {
            result.add(num);
            result.add(delimiter);
        }
        if (result.size() > 0) {
            result.set(result.size() - 1, null); // remove the last delimiter
        }
        return result.stream().filter(Objects::nonNull).collect(Collectors.toList());
    }
}
```

This solution iterates over the input list, adding each number to the result list and then adding the delimiter. It then removes the last delimiter from the result list and returns the list. The `filter` method is used to remove any null elements from the list. The `Collectors.toList()` method is used to collect the filtered elements into a new list. 

This solution assumes that the input list is not empty and that the delimiter is not null. If these assumptions are not valid, additional error checking code would be needed. 

The time complexity of this solution is O(n), where n is the size of the input list, because it iterates over the list once. The space complexity is also O(n), because it creates a new list with the same size as the input list. 