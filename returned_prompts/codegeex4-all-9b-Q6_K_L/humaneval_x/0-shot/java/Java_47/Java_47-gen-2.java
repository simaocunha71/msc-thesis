```java
import java.util.*;
import java.lang.*;

class Solution {
    public double median(List<Integer> l) {
        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 0) {
            return ((double) l.get(n / 2 - 1) + (double) l.get(n / 2)) / 2;
        } else {
            return (double) l.get(n / 2);
        }
    }
}
```