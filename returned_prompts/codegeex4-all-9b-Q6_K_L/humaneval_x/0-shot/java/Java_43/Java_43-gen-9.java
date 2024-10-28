```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean pairsSumToZero(List<Integer> l) {
        Set<Integer> seen = new HashSet<>();
        for (int num : l) {
            if (seen.contains(-num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
```