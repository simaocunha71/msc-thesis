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
        List<Double> sorted = new ArrayList<>(numbers);
        sorted.sort(Double::compareTo);

        List<Double> result = new ArrayList<>();
        result.add(sorted.get(0));
        result.add(sorted.get(1));
        for (int i = 1; i < sorted.size() - 1; i++) {
            if (Math.abs(sorted.get(i) - sorted.get(i - 1)) < Math.abs(sorted.get(i + 1) - sorted.get(i))) {
                continue;
            } else {
                result.set(1, sorted.get(i + 1));
            }
        }
        return result;
    }
}
