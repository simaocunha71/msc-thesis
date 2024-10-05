The problem is asking to find the product of all signs (1, -1, or 0) in the given array and multiply it with the sum of magnitudes of integers in the array. If the array is empty, return None.

Here is a Java solution using the Optional class:

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
            signProduct *= Math.signum(num);
            sumOfMagnitudes += Math.abs(num);
        }
        return Optional.of(signProduct * sumOfMagnitudes);
    }
}
```

In this solution, we first check if the array is empty. If it is, we return an empty Optional. Then, we initialize two variables: signProduct and sumOfMagnitudes. We iterate over the array and for each number, we update signProduct by multiplying it with the sign of the number (using Math.signum) and update sumOfMagnitudes by adding the absolute value of the number (using Math.abs). If we encounter a 0, we return an empty Optional as per the problem statement. Finally, we return an Optional containing the product of signProduct and sumOfMagnitudes. If the array is empty, the Optional will be empty, and if the array is not empty, the Optional will contain the result.