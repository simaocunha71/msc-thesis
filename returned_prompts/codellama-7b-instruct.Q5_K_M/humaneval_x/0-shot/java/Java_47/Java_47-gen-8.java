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
        // Write your code here
        double median = 0;
        int n = l.size();
        Collections.sort(l);
        if (n % 2 == 0) {
            median = (double) ((l.get(n / 2) + l.get(n / 2 - 1)) / 2);
        } else {
            median = (double) l.get(n / 2);
        }
        return median;
    }
}
