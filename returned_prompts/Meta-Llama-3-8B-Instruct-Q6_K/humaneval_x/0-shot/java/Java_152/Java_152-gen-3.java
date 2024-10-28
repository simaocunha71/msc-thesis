Here is a simple Java solution using Java 8 Stream API:

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

In this solution, we use the `stream()` method to create a stream from the `game` list. Then we use the `map()` method to apply a function to each element of the stream. The function calculates the absolute difference between the current score and the corresponding guess score. Finally, we use the `collect()` method to collect the results into a new list.

You can test this method with the examples you provided:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Integer> game1 = Arrays.asList(1, 2, 3, 4, 5, 1);
    List<Integer> guess1 = Arrays.asList(1, 2, 3, 4, 2, -2);
    System.out.println(solution.compare(game1, guess1)); // [0, 0, 0, 0, 3, 3]

    List<Integer> game2 = Arrays.asList(0, 5, 0, 0, 0, 4);
    List<Integer> guess2 = Arrays.asList(4, 1, 1, 0, 0, -2);
    System.out.println(solution.compare(game2, guess2)); // [4, 4, 1, 0, 0, 6]
}
```

This will output the expected results.