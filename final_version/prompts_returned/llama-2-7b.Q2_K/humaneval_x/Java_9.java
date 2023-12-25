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
        // your code here
        int max = -1;
        
        for (int i : numbers ) {
            if (!max.equals(-1))
                max = Math.max(max, i);
            
            System.out.println("rollingMax(Arrays.asList(1, 2, 3, 2, 3, 4, 2)): " + max);
        }
        
        return Arrays.asList(numbers).stream().mapToInt(Integer::intValue).toArray();
    }
    
}