```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        String[] fruits = s.split(" ");
        int apples = Integer.parseInt(fruits[0]);
        int oranges = Integer.parseInt(fruits[4]);
        return n - apples - oranges;
    }
}
```