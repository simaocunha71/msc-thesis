```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        if (lst.size() <= 1) return true;
        int prev = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            int curr = lst.get(i);
            if (curr < prev) return false;
            prev = curr;
        }
        return true;
    }
}
```