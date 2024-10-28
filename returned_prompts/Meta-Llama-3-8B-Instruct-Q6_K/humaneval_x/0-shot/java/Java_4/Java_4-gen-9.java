Here is the solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> meanAbsoluteDeviation(Arrays.asList(1.0, 2.0, 3.0, 4.0))
    1.0
     */
    public double meanAbsoluteDeviation(List<Double> numbers) {
        double mean = 0.0;
        double sum = 0.0;
        for (double num : numbers) {
            sum += num;
        }
        mean = sum / numbers.size();

        double sumMAD = 0.0;
        for (double num : numbers) {
            sumMAD += Math.abs(num - mean);
        }
        return sumMAD / numbers.size();
    }
}
```

This solution calculates the mean of the input numbers and then the Mean Absolute Deviation (MAD) by subtracting the mean from each number, taking the absolute value, and summing up the results. The final result is the sum divided by the size of the input list. The time complexity is O(n), where n is the size of the input list. The space complexity is O(1), as it only uses a constant amount of space to store the mean, sum, and sumMAD variables. 