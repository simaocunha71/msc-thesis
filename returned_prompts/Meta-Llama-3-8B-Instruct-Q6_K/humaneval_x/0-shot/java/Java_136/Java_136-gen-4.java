Here is the Java code that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        List<Optional<Integer>> result = new ArrayList<>();
        
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();
        
        for (Integer num : lst) {
            if (num < 0 && largestNegative.isEmpty()) {
                largestNegative = Optional.of(num);
            } else if (num < 0 && num > largestNegative.get()) {
                largestNegative = Optional.of(num);
            }
            if (num > 0 && smallestPositive.isEmpty()) {
                smallestPositive = Optional.of(num);
            } else if (num > 0 && num < smallestPositive.get()) {
                smallestPositive = Optional.of(num);
            }
        }
        
        result.add(largestNegative);
        result.add(smallestPositive);
        
        return result;
    }
}
```
This solution iterates through the list of integers and keeps track of the largest negative integer and the smallest positive integer. If a negative integer is found and it's larger than the current largest negative integer, it updates the largest negative integer. If a positive integer is found and it's smaller than the current smallest positive integer, it updates the smallest positive integer. Finally, it returns a list containing the largest negative integer and the smallest positive integer as Optional integers. If no negative or positive integers are found, it returns Optional.empty() for both. 