```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        String[] parts = s.split(" and ");
        int apples = Integer.parseInt(parts[0].split(" ")[0]);
        int oranges = Integer.parseInt(parts[1].split(" ")[0]);
        return n - apples - oranges;
    }
}
```
