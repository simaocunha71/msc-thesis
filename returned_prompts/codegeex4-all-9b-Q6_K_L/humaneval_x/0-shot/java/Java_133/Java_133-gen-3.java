```java
import java.util.*;
import java.lang.*;

class Solution {
    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (Double num : lst) {
            sum += Math.pow(Math.ceil(num), 2);
        }
        return sum;
    }
}
```