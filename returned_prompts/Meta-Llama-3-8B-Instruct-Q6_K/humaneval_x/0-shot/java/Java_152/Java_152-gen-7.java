Here is a simple solution in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            result.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return result;
    }
}
```

This solution uses a for loop to iterate over the two lists. For each pair of values, it calculates the absolute difference between the values and adds this to the result list. The absolute difference is used because we want to measure the distance between the two values, regardless of whether the guess was higher or lower than the actual score. The result list is then returned.