```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largestSmallestIntegers(Arrays.asList(2, 4, 1, 3, 5, 7)) == (Optional.empty(), Optional.of(1))
    largestSmallestIntegers(Arrays.asList()) == (Optional.empty(), Optional.empty())
    largestSmallestIntegers(Arrays.asList(0)) == (Optional.empty(), Optional.empty())
     */
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();
        for (Integer i : lst) {
            if (i < 0) {
                if (!largestNegative.isPresent() || i > largestNegative.get()) {
                    largestNegative = Optional.of(i);
                }
            } else if (i > 0) {
                if (!smallestPositive.isPresent() || i < smallestPositive.get()) {
                    smallestPositive = Optional.of(i);
                }
            }
        }
        return Arrays.asList(largestNegative, smallestPositive);
    }
}
```