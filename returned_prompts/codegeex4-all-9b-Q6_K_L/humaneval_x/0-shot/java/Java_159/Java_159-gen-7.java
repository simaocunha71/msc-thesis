```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        int afterMeals = number + need;
        int leftAfterMeals = Math.max(0, remaining - need);
        return Arrays.asList(afterMeals, leftAfterMeals);
    }
}
```