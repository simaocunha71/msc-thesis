```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst) {
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();
        int largestNegativeValue = Integer.MIN_VALUE;
        int smallestPositiveValue = Integer.MAX_VALUE;

        for (int num : lst) {
            if (num < 0 && num > largestNegativeValue) {
                largestNegativeValue = num;
                largestNegative = Optional.of(num);
            } else if (num > 0 && num < smallestPositiveValue) {
                smallestPositiveValue = num;
                smallestPositive = Optional.of(num);
            }
        }

        return Arrays.asList(largestNegative, smallestPositive);
    }
}
```