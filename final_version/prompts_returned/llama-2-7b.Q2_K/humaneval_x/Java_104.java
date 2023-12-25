import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a list of positive integers x. return a sorted list of all
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> uniqueDigits(Arrays.asList(15, 33, 1422, 1))
    [1, 15, 33]
    >>> uniqueDigits(Arrays.asList(152, 323, 1422, 10))
    []
     */
    public List<Integer> uniqueDigits(List<Integer> x) {
        Set<Integer> set = new HashSet<>();
        
        // add any even number to the set.
        if (x.size() == 0) {
            return Collections.synchronizedList(new ArrayList<>());
        }
        for (int i : x) {
            if (!set.add(i)) {
                // only once
                x = Collections.synchronizedList(new ArrayList<>(x));
                break;
            }
        }
        return x;
    }
}