import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescaleToUnit(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0))
    [0.0, 0.25, 0.5, 0.75, 1.0]
     */
    public List<Double> rescaleToUnit(List<Double> numbers) {
        // min and max of the list
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        // create a list to store the result
        List<Double> res = new ArrayList<>();

        // for each number in the original list
        for (double num : numbers) {
            // calculate the relative position of the number between the min and max
            double pos = (num - min) / (max - min);
            res.add(pos);
        }

        return res;
    }
}
