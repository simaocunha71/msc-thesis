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
        double mean = mean(numbers);
        double sum = 0.0;
        for (double x : numbers) {
            sum += Math.abs(x - mean);
        }
        return sum / numbers.size();
    }

    /**
    Calculate mean of a given list of numbers.
    >>> mean(Arrays.asList(1.0, 2.0, 3.0, 4.0))
    2.5
     */
    public double mean(List<Double> numbers) {
        double sum = 0.0;
        for (double x : numbers) {
            sum += x;
        }
        return sum / numbers.size();
    }
}
