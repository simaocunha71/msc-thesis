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
        //Write your code here
        if (numbers == null || numbers.size() < 1) throw new IllegalArgumentException("Invalid input");
        
        Collections.sort(numbers);
        Integer[] pos = new Integer[2];
        for (int i = 0; i < numbers.size(); i++) {
            if (pos[0] != null && pos[1] != null) break;
            Double diff = Math.abs((numbers.get(i)) - (numbers.get(pos[0]) || numbers.get(i)));
            if (diff < 0.001 && i > 0) {
                return new ArrayList<>(Arrays.asList(numbers.get(i), numbers.get(pos[0])));
            } else if (diff < 0.001) {
                pos[0] = i;
                pos[1] = -1;
            }
        }
        
    }
}