import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return sorted unique elements in a list
    >>> unique(Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123))
    [0, 2, 3, 5, 9, 123]
     */
    public List<Integer> unique(List<Integer> l) {
        // write your code here
        Collections.sort(l);
        List<Integer> unique = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            if (i == 0) {
                unique.add(l.get(i));
                continue;
            }
            if (l.get(i) != l.get(i - 1)) {
                unique.add(l.get(i));
            }
        }
        return unique;
    }
}