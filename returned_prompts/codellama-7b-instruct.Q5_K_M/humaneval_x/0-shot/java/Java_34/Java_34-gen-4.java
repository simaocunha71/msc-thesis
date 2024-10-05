import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return sorted unique elements in a list
    >>> unique(Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123))
    [0, 2, 3, 5, 9, 123]
     */
    public List<Integer> unique(List<Integer> l) {
        // Write your code here
        Set<Integer> set = new TreeSet<Integer>(l);
        List<Integer> list = new ArrayList<Integer>(set);
        Collections.sort(list);
        return list;
    }
}
