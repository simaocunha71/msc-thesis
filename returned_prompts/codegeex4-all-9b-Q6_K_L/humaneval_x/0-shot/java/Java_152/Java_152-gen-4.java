```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> diffs = new ArrayList<>(game.size());
        for (int i = 0; i < game.size(); i++) {
            diffs.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return diffs;
    }
}
```
This solution creates a new list called `diffs` with the same size as the input lists. It then iterates over each index of the input lists and calculates the absolute difference between the corresponding elements of `game` and `guess`. This difference is added to the `diffs` list. Finally, the `diffs` list is returned.