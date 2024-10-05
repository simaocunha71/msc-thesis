import java.util.*;
import java.lang.*;

class Solution {
    /**
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> findClosestElements(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0, 2.2))
    [2.0, 2.2]
    >>> findClosestElements(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0, 2.0))
    [2.0, 2.0]
     */
    public List<Double> findClosestElements(List<Double> numbers) {
        if (numbers == null || numbers.size() < 2) {
            throw new IllegalArgumentException("List must contain at least two numbers");
        }
        List<Double> result = new ArrayList<>();
        double minDiff = Double.MAX_VALUE;
        for (int i = 0; i < numbers.size() - 1; i++) {
            double diff = Math.abs(numbers.get(i) - numbers.get(i + 1));
            if (diff < minDiff) {
                minDiff = diff;
                result.clear();
                result.add(numbers.get(i));
                result.add(numbers.get(i + 1));
            } else if (diff == minDiff) {
                result.add(numbers.get(i));
                result.add(numbers.get(i + 1));
            }
        }
        Collections.sort(result);
        return result;
    }
}