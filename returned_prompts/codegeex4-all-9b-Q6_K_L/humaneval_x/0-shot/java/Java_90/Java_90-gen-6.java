Here's how you could solve this problem in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.size() < 2) {
            return Optional.empty();
        }
        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;
        for (int num : lst) {
            if (num < smallest) {
                secondSmallest = smallest;
                smallest = num;
            } else if (num < secondSmallest && num != smallest) {
                secondSmallest = num;
            }
        }
        if (secondSmallest == Integer.MAX_VALUE) {
            return Optional.empty();
        }
        return Optional.of(secondSmallest);
    }
}
```
This solution works by iterating over the list and keeping track of the smallest and second smallest numbers. If the list has fewer than 2 numbers, it returns Optional.empty(). If there is no second smallest number, it returns Optional.empty(). Otherwise, it returns an Optional containing the second smallest number.