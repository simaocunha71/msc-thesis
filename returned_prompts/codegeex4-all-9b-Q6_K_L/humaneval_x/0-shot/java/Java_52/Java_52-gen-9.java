```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean belowThreshold(List<Integer> l, int t) {
        for(int i : l) {
            if(i >= t) return false;
        }
        return true;
    }
}
```