```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if (arr.isEmpty()) {
            return Optional.empty();
        }
        int product = 1;
        int magnitudeSum = 0;
        for (int num : arr) {
            if (num == 0) {
                return Optional.empty();
            }
            product *= num > 0 ? 1 : -1;
            magnitudeSum += Math.abs(num);
        }
        return Optional.of(product * magnitudeSum);
    }
}
```