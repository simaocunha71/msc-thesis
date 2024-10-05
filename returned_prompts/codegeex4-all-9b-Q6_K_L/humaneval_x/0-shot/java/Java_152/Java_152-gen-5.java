```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < game.size(); i++) {
            result.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return result;
    }
}
```
The code creates a new list called `result` and then iterates through the `game` and `guess` lists. For each index `i`, it calculates the absolute difference between the corresponding elements of `game` and `guess` and adds it to `result`. Finally, it returns `result`.