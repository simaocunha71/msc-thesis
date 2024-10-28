```java
import java.util.*;
import java.lang.*;

class Solution {
    public double meanAbsoluteDeviation(List<Double> numbers) {
        if (numbers == null || numbers.size() == 0) {
            return 0.0;
        }

        double mean = calculateMean(numbers);
        double sum = 0.0;
        for (double number : numbers) {
            sum += Math.abs(number - mean);
        }
        return sum / numbers.size();
    }

    private double calculateMean(List<Double> numbers) {
        double sum = 0.0;
        for (double number : numbers) {
            sum += number;
        }
        return sum / numbers.size();
    }
}
```
In the above code, we first check if the input list is null or empty. If so, we return 0.0 as the mean absolute deviation.

We then calculate the mean of the input list using the `calculateMean` method. This method iterates over the list and calculates the sum of all elements, then divides the sum by the size of the list to get the mean.

Next, we iterate over the input list again and calculate the absolute difference between each element and the mean. We add these differences to a running sum.

Finally, we divide the sum by the size of the list to get the mean absolute deviation, and return it.