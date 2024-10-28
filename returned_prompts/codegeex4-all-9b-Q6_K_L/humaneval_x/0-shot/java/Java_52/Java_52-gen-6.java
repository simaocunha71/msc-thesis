Here's the Java implementation:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean belowThreshold(List<Integer> l, int t) {
        for (int i : l) {
            if (i >= t) {
                return false;
            }
        }
        return true;
    }
}
```

This code iterates over each element in the list `l`. If any element is greater than or equal to `t`, the function returns `false`. If all elements are below `t`, the function returns `true`.

This solution is correct and efficient, as it only requires a single pass over the list.