```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> makeAPile(int n) {
        List<Integer> pile = new ArrayList<>();
        int stones = n;
        int level = 1;
        while (stones > 0) {
            pile.add(stones);
            stones += level * 2;
            level++;
        }
        return pile;
    }
}
```