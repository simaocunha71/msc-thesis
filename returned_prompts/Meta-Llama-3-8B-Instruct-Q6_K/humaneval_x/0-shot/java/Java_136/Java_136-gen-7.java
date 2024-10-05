Here is the solution to the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        List<Optional<Integer>> result = new ArrayList<>();
        
        // Initialize two variables to store the largest negative and smallest positive integers
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();
        
        // Iterate over the list to find the largest negative and smallest positive integers
        for (int num : lst) {
            if (num < 0) {
                if (largestNegative.isEmpty() || num > largestNegative.get()) {
                    largestNegative = Optional.of(num);
                }
            } else if (num > 0) {
                if (smallestPositive.isEmpty() || num < smallestPositive.get()) {
                    smallestPositive = Optional.of(num);
                }
            }
        }
        
        // Add the result to the list
        result.add(largestNegative);
        result.add(smallestPositive);
        
        return result;
    }
}
```

This solution iterates over the list to find the largest negative and smallest positive integers. If the list is empty or contains only zeros, it returns two empty Optional values. If the list contains at least one negative integer, it finds the largest one and stores it in the largestNegative variable. If the list contains at least one positive integer, it finds the smallest one and stores it in the smallestPositive variable. Finally, it adds the result to the list and returns it.