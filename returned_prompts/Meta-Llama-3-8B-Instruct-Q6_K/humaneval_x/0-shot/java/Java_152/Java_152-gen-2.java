Here is the solution:

```java
import java.util.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            if (game.get(i) == guess.get(i)) {
                result.add(0);
            } else {
                result.add(Math.abs(game.get(i) - guess.get(i)));
            }
        }
        return result;
    }
}
```


This solution iterates over the two lists and checks if the current elements are equal. If they are, it adds 0 to the result list. If they are not, it calculates the absolute difference between the two elements and adds that to the result list. The result list is then returned.