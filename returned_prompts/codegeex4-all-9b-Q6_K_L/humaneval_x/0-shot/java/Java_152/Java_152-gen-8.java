```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            res.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return res;
    }
}
```