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
        double min = Double.MAX_VALUE;
        double max = Double.MIN_VALUE;

        for (double num : numbers) {
            if (num < min) {
                min = num;
            }
            if (num > max) {
                max = num;
            }
        }

        List<Double> rescaledNumbers = new ArrayList<>();
        for (double num : numbers) {
            rescaledNumbers.add((num - min) / (max - min));
        }

        return rescaledNumbers;
    }
}