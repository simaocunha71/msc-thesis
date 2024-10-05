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
        // calculate mean
        double sum = 0;
        for (Double number : numbers) {
            sum += number;
        }
        double mean = sum / numbers.size();

        // calculate absolute deviation
        double deviation = 0;
        for (Double number : numbers) {
            deviation += Math.abs(number - mean);
        }
        deviation /= numbers.size();

        return deviation;
    }
}

