```java
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> incrList(List<Integer> l) {
        return l.stream()
                .map(i -> i + 1)
                .collect(Collectors.toList());
    }
}
```