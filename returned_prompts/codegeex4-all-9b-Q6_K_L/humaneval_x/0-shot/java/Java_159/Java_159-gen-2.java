```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        int eaten = number + need;
        int left = remaining - need;
        return Arrays.asList(eaten, Math.max(left, 0));
    }
}
```