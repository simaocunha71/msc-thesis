```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        List<Integer> res = new ArrayList<>();
        int total = number + need;
        res.add(total);
        if (need <= remaining) {
            res.add(remaining - need);
        } else {
            res.add(0);
        }
        return res;
    }
}
```