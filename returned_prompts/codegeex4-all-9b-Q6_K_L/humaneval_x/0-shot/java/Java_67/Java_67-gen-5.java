```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        int apples = Integer.parseInt(s.split(" ")[0]);
        int oranges = Integer.parseInt(s.split(" ")[2]);
        return n - apples - oranges;
    }
}
```