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

        // sort the list in ascending order
        Collections.sort(numbers);

        // get the first and last element of the list
        double first = numbers.get(0);
        double last = numbers.get(numbers.size() - 1);

        // find the index of the first element that is not equal to the last element
        int index = 1;
        for (; index < numbers.size(); index++) {
            if (numbers.get(index) != last) {
                break;
            }
        }

        // get the first two elements and return them in a list
        List<Double> result = new ArrayList<>();
        result.add(first);
        result.add(numbers.get(index));
        return result;
    }
}
