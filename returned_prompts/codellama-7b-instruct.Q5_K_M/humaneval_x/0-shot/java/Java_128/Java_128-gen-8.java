import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prodSigns(Arrays.asList(1, 2, 2, -4)) == -9
    >>> prodSigns(Arrays.asList(0, 1)) == 0
    >>> prodSigns(Arrays.asList()) == None
     */
    public Optional<Integer> prodSigns(List<Integer> arr) {
        // your code here
        if (arr.size() == 0) {
            return Optional.empty();
        }
        int res = 0;
        int sign = 1;
        for (Integer i : arr) {
            if (i == 0) {
                sign = 0;
                continue;
            }
            res += Math.abs(i) * sign;
            sign = -sign;
        }
        return Optional.of(res);
    }
}
