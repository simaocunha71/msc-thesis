```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        return x.stream()
                .filter(i -> i.toString().chars().noneMatch(c -> (c - '0') % 2 == 0))
                .sorted()
                .collect(Collectors.toList());
    }
}
```