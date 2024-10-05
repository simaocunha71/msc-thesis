Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){

        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (Integer i : lst) {
            if (i < 0) {
                largestNegative = Optional.of(i < largestNegative.orElse(Integer.MIN_VALUE) ? i : largestNegative.get());
            } else if (i > 0) {
                smallestPositive = Optional.of(i < smallestPositive.orElse(Integer.MAX_VALUE) ? i : smallestPositive.get());
            }
        }

        return Arrays.asList(largestNegative, smallestPositive);
    }
}
```

In this solution, we iterate over the list and check each integer. If it is negative, we update the `largestNegative` if the current integer is smaller than the current `largestNegative`. If it is positive, we update the `smallestPositive` if the current integer is smaller than the current `smallestPositive`. Finally, we return a list of `largestNegative` and `smallestPositive`. If there is no negative or positive integers, `largestNegative` and `smallestPositive` will be empty (i.e., `Optional.empty()`).