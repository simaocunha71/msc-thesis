```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        List<Integer> result = new ArrayList<>();
        int eaten = Math.min(need, remaining);
        result.add(number + eaten);
        result.add(remaining - eaten);
        return result;
    }
}
```