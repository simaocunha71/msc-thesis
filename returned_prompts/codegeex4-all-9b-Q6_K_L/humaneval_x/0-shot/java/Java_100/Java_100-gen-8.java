```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> makeAPile(int n) {
        List<Integer> pile = new ArrayList<>();
        int current = n;
        for (int i = 0; i < n; i++) {
            pile.add(current);
            current += 2;
        }
        return pile;
    }
}
```