
The first question is the only one you've provided code for. The others have no code and only questions. I will review the first question.
Overall, it is a good implementation of the problem, and you've done a good job with it. The only problem is that you've used a nested loop, which is not the most efficient solution for this problem. Instead, you could use a HashSet to store the numbers, and then iterate through the HashSet to find the minimum and maximum numbers. This would be more efficient than using a nested loop.
Here is the updated code:

import java.util.*;
import java.lang.*;

class Solution {
    /**
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
    false
    >>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
    true
     */
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        Set<Double> set = new HashSet<>(numbers);
        double min = Double.MAX_VALUE;
        double max = Double.MIN_VALUE;
        for (Double number : set) {
            if (number < min) {
                min = number;
            }
            if (number > max) {
                max = number;
            }
        }
        return max - min < threshold;
    }
}