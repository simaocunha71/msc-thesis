```java
import java.util.*;
import java.lang.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        int l = 0;
        int r = arr.size() - 1;
        int changes = 0;
        
        while (l < r) {
            if (arr.get(l) != arr.get(r)) {
                changes++;
            }
            l++;
            r--;
        }
        
        return changes;
    }
}
```