import java.util.*;
import java.lang.*;

class Solution {
    public boolean monotonic(List<Integer> l) {
        if (l.size() < 2) return true;

        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) > l.get(i - 1)) {
                decreasing = false;
            } else if (l.get(i) < l.get(i - 1)) {
                increasing = false;
            }
            if (!increasing && !decreasing) return false;
        }

        return increasing || decreasing;
    }
}