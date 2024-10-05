Here is the solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if (arr.isEmpty()) {
            return Optional.empty();
        }

        int signProduct = 1;
        int sumOfMagnitudes = 0;

        for (int num : arr) {
            if (num == 0) {
                return Optional.empty();
            }
            int sign = (num > 0) ? 1 : ((num < 0) ? -1 : 0);
            signProduct *= sign;
            sumOfMagnitudes += Math.abs(num);
        }

        return Optional.of(signProduct * sumOfMagnitudes);
    }
}
```

This solution iterates over the given array and calculates the product of signs and the sum of magnitudes. If the array is empty, it returns an empty optional. If the array contains 0, it returns an empty optional because the product of signs is undefined. Finally, it returns the product of signs and the sum of magnitudes as an optional integer. 

Note: The Optional class is a container that may or may not contain a non-null value. It's used to handle the case where the result of an operation may be null. In this case, we use it to return None for empty arrays. 

The problem statement is not entirely clear, but based on the examples provided, it seems that the function should return None for empty arrays and undefined for arrays containing 0. The function returns the product of signs and the sum of magnitudes for other arrays. 

The unit tests provided check the correctness of the function for different inputs. The function should pass these tests to be considered correct. 

The time complexity of this solution is O(n), where n is the size of the input array. This is because we iterate over the array once to calculate the product of signs and the sum of magnitudes. The space complexity is O(1), which means the space required does not change with the size of the input array. This is because we only use a constant amount of space to store the product of signs and the sum of magnitudes. 