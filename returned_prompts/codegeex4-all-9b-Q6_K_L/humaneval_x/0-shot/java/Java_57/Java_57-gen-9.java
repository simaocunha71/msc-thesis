```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean monotonic(List<Integer> l) {
        if (l.size() < 2) {
            return true;
        }
        int direction = 0;
        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) > l.get(i - 1)) {
                if (direction < 0) {
                    return false;
                }
                direction = 1;
            } else if (l.get(i) < l.get(i - 1)) {
                if (direction > 0) {
                    return false;
                }
                direction = -1;
            }
        }
        return true;
    }
}
```