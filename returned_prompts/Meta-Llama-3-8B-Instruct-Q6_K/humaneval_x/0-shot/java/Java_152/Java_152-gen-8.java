Here is the Java solution for the problem:

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

This solution iterates over the game and guess lists simultaneously using a for loop. For each match, it checks if the guess matches the game score. If they match, it adds 0 to the result list. If they don't match, it calculates the absolute difference between the guess and the game score and adds it to the result list. Finally, it returns the result list.