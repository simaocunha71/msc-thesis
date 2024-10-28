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
        int sum = 0;
        int prod = 1;
        for (int num : arr) {
            sum += Math.abs(num);
            prod *= Math.signum(num);
        }
        return prod == 0 ? Optional.empty() : Optional.of(sum * prod);
    }
}