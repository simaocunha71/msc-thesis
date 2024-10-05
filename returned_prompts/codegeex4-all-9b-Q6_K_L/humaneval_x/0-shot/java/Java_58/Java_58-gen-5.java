```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        l1.retainAll(l2);
        Collections.sort(l1);
        return l1;
    }
}
```