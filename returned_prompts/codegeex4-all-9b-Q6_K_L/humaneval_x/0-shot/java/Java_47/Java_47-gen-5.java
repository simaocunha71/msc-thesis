import java.util.*;
import java.lang.*;

class Solution {
    public double median(List<Integer> l) {
        double median = 0.0;
        Collections.sort(l);
        if (l.size() % 2 == 0) {
            median = (l.get(l.size() / 2 - 1) + l.get(l.size() / 2)) / 2.0;
        } else {
            median = l.get(l.size() / 2);
        }
        return median;
    }
}