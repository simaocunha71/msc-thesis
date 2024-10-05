```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        String[] parts = s.split(" ");
        int apples = Integer.parseInt(parts[0]);
        int oranges = Integer.parseInt(parts[4]);
        return n - apples - oranges;
    }
}
```
