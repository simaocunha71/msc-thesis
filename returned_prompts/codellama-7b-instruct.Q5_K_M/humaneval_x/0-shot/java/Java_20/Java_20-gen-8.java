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
            return null;
        }
        Collections.sort(numbers);
        List<Double> closest = new ArrayList<Double>(2);
        closest.add(numbers.get(0));
        closest.add(numbers.get(1));
        double minDelta = Math.abs(closest.get(0) - closest.get(1));
        for (int i = 1; i < numbers.size() - 1; i++) {
            double delta = Math.abs(closest.get(0) - numbers.get(i));
            if (delta < minDelta) {
                minDelta = delta;
                closest.set(1, numbers.get(i));
            } else {
                delta = Math.abs(closest.get(1) - numbers.get(i));
                if (delta < minDelta) {
                    minDelta = delta;
                    closest.set(0, numbers.get(i));
                }
            }
        }
        return closest;
    }
}
