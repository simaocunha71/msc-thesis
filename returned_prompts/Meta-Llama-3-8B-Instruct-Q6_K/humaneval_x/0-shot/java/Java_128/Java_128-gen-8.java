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
            if (num != 0) {
                signProduct *= Math.signum(num);
                sumOfMagnitudes += Math.abs(num);
            }
        }
        return Optional.of(sumOfMagnitudes * signProduct);
    }
}
```

This solution first checks if the array is empty. If it is, the function returns an empty optional. If the array is not empty, it calculates the product of the signs of all numbers in the array and the sum of the absolute values of all numbers in the array. Finally, it returns an optional containing the product of the signs and the sum of the magnitudes. The `Math.signum` function is used to get the sign of a number (1 for positive, -1 for negative, 0 for zero). The `Math.abs` function is used to get the absolute value of a number. The `Optional` class is used to handle the case where the input array is empty. If the array is empty, the function returns an empty optional. If the array is not empty, the function returns an optional containing the result. The `Optional.of` function is used to create an optional containing the result. The `Optional.empty` function is used to create an empty optional. The `if (num != 0)` condition is used to skip the case where the number is zero, because the sign of zero is undefined. The `signProduct *= Math.signum(num);` line is used to update the product of the signs. The `sumOfMagnitudes += Math.abs(num);` line is used to update the sum of the absolute values. The `return Optional.of(sumOfMagnitudes * signProduct);` line is used to return the result. The `return Optional.empty();` line is used to return an empty optional if the array is empty. The `Optional` class is a container that may or may not contain a non-null value. If it contains a value, it is called a non-empty optional. If it does not contain a value, it is called an empty optional. The `Optional` class is used to handle the case where the input array is empty. If the