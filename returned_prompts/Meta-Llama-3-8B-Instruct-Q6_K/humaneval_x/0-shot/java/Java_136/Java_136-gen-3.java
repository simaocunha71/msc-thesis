Here is the solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        Optional<Integer> maxNeg = Optional.empty();
        Optional<Integer> minPos = Optional.empty();

        for (int num : lst) {
            if (num < 0) {
                if (maxNeg.isPresent()) {
                    if (num > maxNeg.get()) {
                        maxNeg = Optional.of(num);
                    }
                } else {
                    maxNeg = Optional.of(num);
                }
            } else if (num > 0) {
                if (minPos.isPresent()) {
                    if (num < minPos.get()) {
                        minPos = Optional.of(num);
                    }
                } else {
                    minPos = Optional.of(num);
                }
            }
        }

        List<Optional<Integer>> result = new ArrayList<>();
        result.add(maxNeg);
        result.add(minPos);

        return result;
    }
}
```

This solution iterates through the list of integers. If it finds a negative number, it checks if the current maximum negative number is greater than the current number. If it is, it updates the maximum negative number. If it finds a positive number, it does the same but for the minimum positive number. If it doesn't find any negative or positive numbers, it returns them as Optional.empty(). Finally, it returns the list of Options. 