```java
import java.util.*;
import java.lang.*;

class Solution {
    public int maxElement(List<Integer> l) {
        if (l == null || l.size() == 0) {
            throw new IllegalArgumentException("List must not be null or empty");
        }
        int max = l.get(0);
        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) > max) {
                max = l.get(i);
            }
        }
        return max;
    }
}
```