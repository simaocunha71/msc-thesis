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

        // sort the list first
        Collections.sort(numbers);

        // find the min and max
        double min = numbers.get(0);
        double max = numbers.get(numbers.size() - 1);

        // create the result list
        List<Double> res = new ArrayList<Double>(numbers.size());

        // rescale the number in place
        for (int i = 0; i < numbers.size(); i++) {
            res.add((numbers.get(i) - min) / (max - min));
        }

        // return the result list
        return res;
    }
}
