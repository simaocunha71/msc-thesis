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
        // write your code here
        List<Double> list = new ArrayList();
        double min = Collections.min(numbers);
        double max = Collections.max(numbers);
        double range = max - min;
        for (Double number : numbers) {
            double d = (number - min) / range;
            list.add(d);
        }
        return list;
    }
}
