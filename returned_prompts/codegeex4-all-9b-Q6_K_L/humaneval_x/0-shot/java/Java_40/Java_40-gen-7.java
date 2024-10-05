```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean triplesSumToZero(List<Integer> l) {
        Set<Integer> set = new HashSet<>(l);
        for (int i : l) {
            for (int j : l) {
                if (i != j && set.contains(-i - j)) {
                    return true;
                }
            }
        }
        return false;
    }
}
```