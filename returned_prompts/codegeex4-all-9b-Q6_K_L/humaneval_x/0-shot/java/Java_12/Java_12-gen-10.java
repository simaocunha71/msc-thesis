```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        return strings.stream()
            .reduce((s1, s2) -> s1.length() >= s2.length() ? s1 : s2);
    }
}
```