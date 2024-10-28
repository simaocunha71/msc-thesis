```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        int product = 1;
        int signProduct = 1;
        int zeroCount = 0;

        for (int num : arr) {
            if (num == 0) {
                zeroCount++;
            } else {
                product *= Math.abs(num);
                signProduct *= (num > 0) ? 1 : -1;
            }
        }

        if (zeroCount > 0) {
            return Optional.empty();
        } else {
            return Optional.of(product * signProduct);
        }
    }
}
```