import java.util.*;

class Solution {
    public int maxElement(List<Integer> l) {
        int max = Integer.MIN_VALUE;
        for (int i : l) {
            if (i > max) {
                max = i;
            }
        }
        return max;
    }
}
