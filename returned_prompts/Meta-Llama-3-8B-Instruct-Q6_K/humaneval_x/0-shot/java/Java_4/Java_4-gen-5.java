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
        double sum = 0;
        double mean = 0;
        for (Double number : numbers) {
            sum += Math.abs(number - mean);
            mean += number;
        }
        mean /= numbers.size();
        return sum / numbers.size();
    }
}
```
In this solution, we first calculate the mean of the input numbers. Then, for each number, we calculate the absolute difference between the number and the mean, and add it to the sum. Finally, we return the average of the absolute differences, which is the Mean Absolute Deviation.  



