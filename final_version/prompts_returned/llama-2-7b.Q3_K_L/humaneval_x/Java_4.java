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
        // write your code here
        double sum = 0;
        
        
        for (int i=0 ; i < numbers.size() - 1; i++)
            sum += Math.abs(numbers.get(i) - numbers.get(i+1));
        
        return sum/((numbers.size() - 1)*2);
    }
}
