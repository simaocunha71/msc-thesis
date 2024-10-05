```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        int last = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < last) {
                return false;
            }
            last = lst.get(i);
        }
        return true;
    }
}
```