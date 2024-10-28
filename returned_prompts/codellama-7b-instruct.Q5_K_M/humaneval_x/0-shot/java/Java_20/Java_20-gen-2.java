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
        // TODO: Implement this method
        if (numbers.size() < 2) {
            return numbers;
        }
        Collections.sort(numbers);
        List<Double> result = new ArrayList<Double>();
        result.add(numbers.get(0));
        result.add(numbers.get(1));
        int n = numbers.size();
        double diff = numbers.get(1) - numbers.get(0);
        double currentDiff;
        for (int i = 2; i < n; i++) {
            currentDiff = numbers.get(i) - numbers.get(i - 1);
            if (currentDiff < diff) {
                diff = currentDiff;
                result.set(1, numbers.get(i));
            }
        }
        return result;
    }
}
