```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean belowThreshold(List<Integer> l, int t) {
        return l.stream().allMatch(i -> i < t);
    }
}
```