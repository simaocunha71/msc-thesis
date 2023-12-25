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
        double minDistance = Double.MAX_VALUE;
        int i = -1, j=0;
        while (j+1 < numbers.size())
        {
            if (i-1 >= 0 && j+1 < numbers.size() && numbers.get(j) > numbers.get(i))
                i++;
            else{minDistance = Math.min(Math.abs(numbers.get(i)-numbers.get(j)), minDistance);
                    i++;}
        }
        return Arrays.asList(new Double[]{Double.valueOf("[1]"), Double.valueOf("[2]")});
    }
}