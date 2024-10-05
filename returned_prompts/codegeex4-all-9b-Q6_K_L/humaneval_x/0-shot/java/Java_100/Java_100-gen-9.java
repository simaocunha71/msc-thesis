```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> makeAPile(int n) {
        List<Integer> levels = new ArrayList<>();
        int stones = n;
        for (int i = 0; i < n; i++) {
            levels.add(stones);
            stones += 2;
        }
        return levels;
    }
}
```