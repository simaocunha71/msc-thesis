import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic(Arrays.asList(1, 2, 4, 20))
    true
    >>> monotonic(Arrays.asList(1, 20, 4, 10))
    false
    >>> monotonic(Arrays.asList(4, 1, 0, -10))
    true
     */
    public boolean monotonic(List<Integer> l) {
        if (l == null || l.size() < 2) return true;
        return isAscending(l);
    }

    private boolean isAscending(List<Integer> l){
        Iterator<Integer> it = l.iterator();
        while(it.hasNext()) {
            int a = it.next();
            if (a < it.previous().intValue() || !isStrictlyIncreasing(l, a)) return false;
        }
        return true;
    }

    private boolean isStrictlyIncreasing(List<Integer> l, int num){
        Iterator<Integer> it = l.iterator();
        while(it.hasNext()) {
            if (l.indexOf(num) == 0 && !it.previous().intValue() > num || it.next().intValue() < num) return false;
        }
        return true;
    }
}
