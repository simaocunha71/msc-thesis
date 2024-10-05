```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < lst.size(); i++) {
            if (i > 0 && lst.get(i) < lst.get(i - 1)) {
                return false;
            }
            if (!set.add(lst.get(i))) {
                return false;
            }
        }
        return true;
    }
}
```