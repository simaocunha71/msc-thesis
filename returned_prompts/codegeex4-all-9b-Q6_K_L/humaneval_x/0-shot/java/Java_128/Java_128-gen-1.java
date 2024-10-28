Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if(arr.size() == 0) {
            return Optional.empty();
        }
        int productSign = 1;
        int sum = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) == 0) {
                return Optional.of(0);
            }
            if (arr.get(i) < 0) {
                productSign *= -1;
            }
            sum += Math.abs(arr.get(i));
        }
        return Optional.of(productSign * sum);
    }
}
```

In this solution, we first check if the array is empty. If it is, we return an empty Optional.

Next, we initialize the productSign to 1 and the sum to 0.

Then, we iterate over the array. If we encounter a 0, we return an Optional of 0, since the product of any number with 0 is 0.

If we encounter a negative number, we multiply the productSign by -1. This is because the product of two negative numbers is positive, and the product of a negative number and a positive number is negative.

Finally, we add the absolute value of the current number to the sum.

After we have iterated over all the numbers, we return an Optional of the product of the productSign and the sum.