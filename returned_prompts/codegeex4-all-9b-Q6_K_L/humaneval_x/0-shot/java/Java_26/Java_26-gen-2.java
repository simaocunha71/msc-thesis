```java
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        return numbers.stream()
                      .filter(i -> Collections.frequency(numbers, i) == 1)
                      .collect(Collectors.toList());
    }
}
```
