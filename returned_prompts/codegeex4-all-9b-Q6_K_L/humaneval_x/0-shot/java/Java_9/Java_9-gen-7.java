import java.util.*;
import java.lang.*;

class Solution {
    /**
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rollingMax(Arrays.asList(1, 2, 3, 2, 3, 4, 2))
    [1, 2, 3, 3, 3, 4, 4]
     */
    public List<Integer> rollingMax(List<Integer> numbers) {
        int max = Integer.MIN_VALUE;
        List<Integer> result = new ArrayList<>();
        for (int num : numbers) {
            max = Math.max(max, num);
            result.add(max);
        }
        return result;
    }
}