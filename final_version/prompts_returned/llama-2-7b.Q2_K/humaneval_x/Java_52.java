import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return True if all numbers in the list l are below threshold t.
    >>> belowThreshold(Arrays.asList(1, 2, 4, 10), 100)
    true
    >>> belowThreshold(Arrays.asList(1, 20, 4, 10), 5)
    false
     */
    public boolean belowThreshold(List<Integer> l, int t) {
        if (l == null || l.isEmpty()) return true;
        if ((t != 0 && t > Integer.MAX_VALUE / (double)l.size())) // t is too big to use
            return false;
        Collections.sort(l);
        
        for (int i = 0; i < l.size() - 1; i++) {// Check each element
                if ((t > Integer.MAX_VALUE / (double)i || t <= (double)(i + 1)) && l.get(i) >= t) {
                    return false;
                }
        }
        return true;
    }
}