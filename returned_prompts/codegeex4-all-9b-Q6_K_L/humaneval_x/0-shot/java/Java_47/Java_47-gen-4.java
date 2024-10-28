import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return median of elements in the list l.
    >>> median(Arrays.asList(3, 1, 2, 4, 5))
    3
    >>> median(Arrays.asList(-10, 4, 6, 1000, 10, 20))
    15.0
     */
    public double median(List<Integer> l) {
        if (l == null || l.size() == 0) {
            throw new IllegalArgumentException("List is empty");
        }
        Collections.sort(l);
        int size = l.size();
        if (size % 2 == 0) {
            return (l.get(size / 2 - 1) + l.get(size / 2)) / 2.0;
        } else {
            return l.get(size / 2);
        }
    }
}