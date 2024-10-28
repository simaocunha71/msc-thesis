```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        int total = number + need;
        if (total > remaining) {
            total = remaining;
        }
        int left = remaining - total;
        return Arrays.asList(total, left);
    }
}
```