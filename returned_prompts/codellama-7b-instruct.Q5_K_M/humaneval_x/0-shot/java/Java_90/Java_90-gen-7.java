import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a list of integers.
    Write a function nextSmallest() that returns the 2nd smallest element of the list.
    Return null if there is no such element.
    <p>
    nextSmallest(Arrays.asList(1, 2, 3, 4, 5)) == Optional[2]
    nextSmallest(Arrays.asList(5, 1, 4, 3, 2)) == Optional[2]
    nextSmallest(Arrays.asList()) == Optional.empty
    nextSmallest(Arrays.asList(1, 1)) == Optional.empty
     */
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        // write your code here
        int min = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;
        for (int x : lst) {
            if (x < min) {
                secondMin = min;
                min = x;
            } else if (x < secondMin && x != min) {
                secondMin = x;
            }
        }
        if (secondMin == Integer.MAX_VALUE) {
            return Optional.empty();
        }
        return Optional.of(secondMin);
    }
}
