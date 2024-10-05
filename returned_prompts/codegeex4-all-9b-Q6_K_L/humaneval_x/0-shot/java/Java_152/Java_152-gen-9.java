```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < game.size(); i++) {
            result.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return result;
    }
}
```
This solution iterates through the game and guess lists and adds the absolute difference between the corresponding elements to the result list. The absolute difference is calculated using the Math.abs() method. The result list is then returned.