Here's the Java code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if (arr.isEmpty()) {
            return Optional.empty();
        }

        int prodSign = 1;
        int sumMagnitude = 0;

        for (int num : arr) {
            if (num == 0) {
                return Optional.of(0);
            }
            if (num < 0) {
                prodSign *= -1;
            }
            sumMagnitude += Math.abs(num);
        }

        return Optional.of(prodSign * sumMagnitude);
    }
}
```

This code works by iterating over each number in the array. If the number is zero, it returns 0 immediately. If the number is negative, it multiplies the prodSign by -1. It adds the absolute value of the number to the sumMagnitude. Finally, it returns the product of prodSign and sumMagnitude as an Optional.