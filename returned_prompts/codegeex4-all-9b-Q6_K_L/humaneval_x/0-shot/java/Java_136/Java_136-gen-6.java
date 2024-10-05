Here's how you could write the function in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();

        for (int num : lst) {
            if (num < 0 && (!largestNegative.isPresent() || num > largestNegative.get())) {
                largestNegative = Optional.of(num);
            }
            if (num > 0 && (!smallestPositive.isPresent() || num < smallestPositive.get())) {
                smallestPositive = Optional.of(num);
            }
        }

        return Arrays.asList(largestNegative, smallestPositive);
    }
}
```

In this function, we use two Optional variables to keep track of the largest negative and smallest positive numbers. We iterate over the list of numbers and update these variables as we find larger negative numbers or smaller positive numbers. At the end, we return a list of these two Optional variables.