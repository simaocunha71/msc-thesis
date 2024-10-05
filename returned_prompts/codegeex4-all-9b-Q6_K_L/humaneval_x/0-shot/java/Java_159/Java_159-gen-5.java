```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        int[] result = new int[2];
        result[0] = number + need;
        result[1] = remaining - need;
        return Arrays.stream(result).boxed().collect(Collectors.toList());
    }
}
```