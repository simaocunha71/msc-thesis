```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> makeAPile(int n) {
        List<Integer> pile = new ArrayList<>();
        int stones = n;
        for (int i = 0; i < n; i++) {
            pile.add(stones);
            stones += (i % 2 == 0) ? 2 : 1;
        }
        return pile;
    }
}
```