```java
import java.util.*;
import java.lang.*;

class Solution {
    public int maxElement(List<Integer> l) {
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < l.size(); i++) {
            if (l.get(i) > max) {
                max = l.get(i);
            }
        }
        return max;
    }
}
```