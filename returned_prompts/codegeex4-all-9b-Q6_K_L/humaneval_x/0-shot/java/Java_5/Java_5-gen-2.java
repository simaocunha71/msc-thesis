```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        if (numbers.isEmpty()) {
            return Collections.emptyList();
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.size() - 1; i++) {
            result.add(numbers.get(i));
            result.add(delimiter);
        }
        result.add(numbers.get(numbers.size() - 1));

        return result;
    }
}
```