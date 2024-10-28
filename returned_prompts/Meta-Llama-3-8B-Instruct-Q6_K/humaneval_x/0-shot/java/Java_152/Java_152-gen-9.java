The problem is asking to calculate the difference between the actual scores and the guessed scores for a series of matches. The result should be an array of the same length as the input arrays, where each element is the absolute difference between the actual score and the guessed score for that match.

Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            if (game.get(i).equals(guess.get(i))) {
                result.add(0);
            } else {
                result.add(Math.abs(game.get(i) - guess.get(i)));
            }
        }
        return result;
    }
}
```

This solution uses a for loop to iterate over the input arrays. For each match, it checks if the actual score equals the guessed score. If it does, it adds 0 to the result list. If not, it calculates the absolute difference between the actual score and the guessed score and adds it to the result list. Finally, it returns the result list.