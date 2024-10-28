Here is the solution in Java:
```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst) {
        List<Optional<Integer>> result = new ArrayList<>();

        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (int num : lst) {
            if (num < 0 && (largestNegative.isEmpty() || num > largestNegative.get())) {
                largestNegative = Optional.of(num);
            } else if (num > 0 && (smallestPositive.isEmpty() || num < smallestPositive.get())) {
                smallestPositive = Optional.of(num);
            }
        }

        result.add(largestNegative);
        result.add(smallestPositive);

        return result;
    }
}
```
In this solution, we iterate through the list of integers and keep track of the largest negative integer and the smallest positive integer. If we find a negative integer that is larger than the current largest negative integer, we update the largest negative integer. Similarly, if we find a positive integer that is smaller than the current smallest positive integer, we update the smallest positive integer. Finally, we return the largest negative integer and the smallest positive integer as a list of Optional integers. If there are no negative or positive integers, the Optional will be empty.