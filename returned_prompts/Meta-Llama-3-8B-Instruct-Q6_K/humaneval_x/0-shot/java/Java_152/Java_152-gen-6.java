You can use Java streams to solve this problem. Here's the solution:

```java
import java.util.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        return game.stream()
                .map((score, index) -> Math.abs(score - guess.get(index)))
                .collect(Collectors.toList());
    }
}
```

This solution works by mapping each score in the game list to the absolute difference between the score and the corresponding guess in the guess list. The `map` function takes a function that takes two arguments, the first being an element of the game list and the second being the index of that element. It then applies this function to each element of the game list, effectively calculating the absolute difference between the score and the guess for each match. The result is a stream of integers representing the differences. The `collect` function is then used to collect these differences into a list, which is the final result.