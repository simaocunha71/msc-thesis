```java
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution {
    public List<Integer> getPositive(List<Integer> l) {
        return l.stream().filter(i -> i > 0).collect(Collectors.toList());
    }
}
```