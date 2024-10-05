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

        int size = numbers.size();
        List<Integer> result = new ArrayList<Integer>(size);
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < size; i++) {
            if(max < numbers.get(i)) max = numbers.get(i);
            result.add(max);
        }
        return result;
    }
}