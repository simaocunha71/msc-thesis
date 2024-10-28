The task is to calculate the sum of squared numbers in a given list, rounding each element to the upper integer (ceiling) first.

Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (Double num : lst) {
            int ceiling = (int) Math.ceil(num);
            sum += ceiling * ceiling;
        }
        return sum;
    }
}
```
Explanation:

1. Initialize a variable `sum` to 0, which will store the sum of squared numbers.
2. Iterate through the given list `lst` using a for-each loop.
3. For each number `num` in the list, use the `Math.ceil` function to round the number to the upper integer (ceiling).
4. Calculate the square of the rounded number (`ceiling * ceiling`) and add it to the `sum`.
5. Return the `sum` as the result.

This solution works correctly for both positive and negative numbers, as well as for numbers with decimal points. The `Math.ceil` function ensures that each number is rounded to the upper integer, as required.