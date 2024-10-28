Here is the solution to the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if (arr.isEmpty()) {
            return Optional.empty();
        }

        int sign = 1;
        int sum = 0;

        for (int num : arr) {
            if (num == 0) {
                return Optional.empty();
            }
            if (num < 0) {
                sign *= -1;
            }
            sum += Math.abs(num);
        }

        return Optional.of(sign * sum);
    }
}
```

This solution iterates over the input list to calculate the product of signs and the sum of magnitudes of integers. If the list is empty, it returns an empty optional. If the list contains zero, it also returns an empty optional. Otherwise, it returns an optional containing the product of signs and the sum of magnitudes. The `Optional` class is used to handle the possibility of an empty list or a list containing zero. The `Optional.empty()` method is used to create an empty optional, and the `Optional.of()` method is used to create an optional containing a value. The `Math.abs()` method is used to calculate the magnitude of each integer. The product of signs is calculated by multiplying the sign of each integer, and the sum of magnitudes is calculated by adding the magnitudes of each integer. The product of signs and the sum of magnitudes are then returned in an optional.