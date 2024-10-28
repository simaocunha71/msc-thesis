```java
import java.util.*;

class Solution {
    public double meanAbsoluteDeviation(List<Double> numbers) {
        double mean = 0.0;
        for (double num : numbers) {
            mean += num;
        }
        mean /= numbers.size();

        double sum = 0.0;
        for (double num : numbers) {
            sum += Math.abs(num - mean);
        }
        return sum / numbers.size();
    }
}
```

Explanation:

1. Calculate the mean of the list of numbers by summing all the numbers and then dividing by the size of the list.
2. Initialize a sum variable to 0.0 to store the sum of absolute deviations.
3. Iterate over the list of numbers again, this time calculating the absolute deviation of each number from the mean.
4. Add the absolute deviation to the sum variable.
5. Calculate the mean absolute deviation by dividing the sum of absolute deviations by the size of the list.

The time complexity of this solution is O(n), where n is the size of the input list, because we iterate over the list twice. The space complexity is O(1), because we only use a constant amount of space to store the mean and sum variables. 