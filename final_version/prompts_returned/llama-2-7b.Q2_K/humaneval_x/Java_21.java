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
        if (numbers == null || numbers.size() < 2) return numbers;
        
        // Fill with zeros
        for (int i=0; i<5-numbers.size(); i++) numbers.add(0);
        
        // Scale so that the smallest becomes 0 and the largest becomes 1, in order
        for (Double n: numbers) { n *= Math.max(1.0/numbers.get(numbers.size()-1),1.0/(n==numbers.get(0)-1?1:n)); }
        
        return numbers;
    }
}
