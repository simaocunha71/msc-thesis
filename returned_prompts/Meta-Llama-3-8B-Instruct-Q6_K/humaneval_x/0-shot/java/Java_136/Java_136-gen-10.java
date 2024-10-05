Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst) {
        List<Optional<Integer>> result = new ArrayList<>();
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (int num : lst) {
            if (num < 0 && largestNegative.isEmpty() || num > largestNegative.get()) {
                largestNegative = Optional.of(num);
            }
            if (num > 0 && smallestPositive.isEmpty() || num < smallestPositive.get()) {
                smallestPositive = Optional.of(num);
            }
        }

        result.add(largestNegative);
        result.add(smallestPositive);

        return result;
    }
}
```

This solution iterates over the list of integers, and for each integer, it checks if it's the largest negative integer or the smallest positive integer. If it is, it updates the corresponding optional variable. Finally, it returns a list of these two optional variables. If there are no negative or positive integers in the list, it returns two empty optionals. 

The time complexity of this solution is O(n), where n is the size of the input list, because it iterates over the list once. The space complexity is O(1), because it uses a constant amount of space to store the result and the optional variables, regardless of the size of the input list. 