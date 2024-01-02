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
        int max = Integer.MIN_VALUE;
        long currSum = 0L;
        List<Long> result = new ArrayList<>();

        for (int i = 1; i < numbers.size(); i++) {
            if (currSum >= max) {
                result.add(max);
                max = Integer.MIN_VALUE;
                currSum = 0L;
            } else {
                int a = numbers.get(i - 1), b = numbers.get(i);
                long sum = a + (b > max ? b : max) + (b < max ? -(max - b) : 0);
                currSum += sum;
            }
        }
        
        if (currSum >= max) {
            result.add(max);
        } else {
            int a = numbers.get(numbers.size()-1), b = numbers.get(numbers.size());
            long sum = a + (b > max ? b : max) + (b < max ? -(max - b) : 0);
            currSum += sum;
        }
        
        return result;
    }
}