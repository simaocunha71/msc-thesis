Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst) {
        List<Optional<Integer>> result = new ArrayList<>();
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (Integer num : lst) {
            if (num < 0) {
                if (!largestNegative.isPresent() || num > largestNegative.get()) {
                    largestNegative = Optional.of(num);
                }
            } else if (num > 0) {
                if (!smallestPositive.isPresent() || num < smallestPositive.get()) {
                    smallestPositive = Optional.of(num);
                }
            }
        }

        result.add(largestNegative);
        result.add(smallestPositive);

        return result;
    }
}
```

This solution iterates over the given list of integers. If a negative integer is found, it checks if it's the largest negative integer found so far. If it is, it updates the `largestNegative` Optional. Similarly, if a positive integer is found, it checks if it's the smallest positive integer found so far. If it is, it updates the `smallestPositive` Optional. Finally, it returns a list containing the `largestNegative` and `smallestPositive` Optionsals. If no negative or positive integers are found, the corresponding Optionals remain empty.