import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return sorted unique elements in a list
    >>> unique(Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123))
    [0, 2, 3, 5, 9, 123]
     */
    public List<Integer> unique(List<Integer> l) {
        // Sort the list
        Collections.sort(l);

        // Remove duplicates
        List<Integer> unique = new ArrayList<>();
        for (Integer i : l) {
            if (!unique.contains(i)) {
                unique.add(i);
            }
        }

        return unique;
    }
}