```java
import java.util.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        int totalEaten = number + need;
        int carrotsLeft = remaining - (need - number);
        if (carrotsLeft < 0) {
            totalEaten += remaining;
            carrotsLeft = 0;
        }
        return Arrays.asList(totalEaten, carrotsLeft);
    }
}
```

Explanation:

The function `eat` takes three parameters: `number` (the number of carrots already eaten), `need` (the number of carrots needed to be eaten), and `remaining` (the number of carrots remaining in stock).

First, we calculate the total number of carrots eaten by adding `number` and `need`. This represents the total number of carrots consumed.

Then, we calculate the number of carrots left by subtracting the difference between `need` and `number` from `remaining`. If the result is negative, it means that we have eaten more carrots than remaining, so we set the carrots left to 0 and add the remaining carrots to the total eaten.

Finally, we return a list containing the total eaten and the carrots left. This list represents the solution to the problem.