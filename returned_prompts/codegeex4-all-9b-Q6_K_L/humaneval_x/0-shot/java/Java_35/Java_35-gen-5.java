```java
import java.util.*;
import java.lang.*;

class Solution {
    public int maxElement(List<Integer> l) {
        if (l == null || l.isEmpty()) {
            throw new IllegalArgumentException("List is null or empty");
        }
        return Collections.max(l);
    }
}
```