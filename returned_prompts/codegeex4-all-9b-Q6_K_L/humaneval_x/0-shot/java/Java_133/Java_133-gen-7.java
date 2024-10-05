```java
import java.util.*;
import java.lang.*;

class Solution {
    public int sumSquares(List<Double> lst) {
        return lst.stream()
            .mapToInt(d -> (int) Math.ceil(d))
            .map(i -> i * i)
            .sum();
    }
}
```