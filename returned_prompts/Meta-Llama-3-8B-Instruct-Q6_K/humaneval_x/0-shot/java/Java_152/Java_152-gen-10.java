Here is a Java solution that uses the Java 8 Stream API to solve the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        return game.stream()
                .map((score, guessScore) -> Math.abs(guessScore - score))
                .collect(Collectors.toList());
    }
}
```

This solution works by using the `stream()` method to create a stream from the `game` list. The `map()` method is then used to create a new stream where each element is the absolute difference between the corresponding elements in the `game` and `guess` lists. The `collect()` method is used to collect the elements of the stream into a new list, which is returned as the result.