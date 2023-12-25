import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return sorted unique common elements for two lists.
    >>> common(Arrays.asList(1, 4, 3, 34, 653, 2, 5), Arrays.asList(5, 7, 1, 5, 9, 653, 121))
    [1, 5, 653]
    >>> common(Arrays.asList(5, 3, 2, 8), Arrays.asList(3, 2))
    [2, 3]
     */
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        Set<Integer> set = new HashSet<>();
        for (int e :l1) {
            if (!set.contains(e)) set.add(e);
        }
        if (set.size() == 0) return Collections.emptyList();
        
        List<Integer> res = new ArrayList<>();
        for (Integer e : l2) {
            if (set.contains(e)) res.add(e);
        }
        return res;
    }
}
