```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        return strings.stream()
                .max(Comparator.comparing(String::length));
    }
}
```