Here is the Java code to solve the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < game.size(); i++) {
            int diff = Math.abs(game.get(i) - guess.get(i));
            result.add(diff);
        }
        return result;
    }
}
```

This code iterates over the two input lists, calculates the absolute difference between each score and its corresponding guess, and adds the result to a new list. This list is then returned as the solution. 

For example, if the input lists are [1,2,3,4,5,1] and [1,2,3,4,2,-2], the output list will be [0,0,0,0,3,3], because the guesses for the first four matches were correct, and the guesses for the last two matches were 3 and 3 units off, respectively. If the input lists are [0,5,0,0,0,4] and [4,1,1,0,0,-2], the output list will be [4,4,1,0,0,6], because the guesses for the first two matches were 4 units off, the third match was 1 unit off, and the last three matches were correct. 

This solution has a time complexity of O(n), where n is the size of the input lists, because it iterates over the lists once. The space complexity is also O(n), because it creates a new list to store the results. 