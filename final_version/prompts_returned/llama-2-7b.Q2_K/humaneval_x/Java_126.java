import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return false. Assume no negative numbers and only integers.

    Examples
    isSorted(Arrays.asList(5)) -> true
    isSorted(Arrays.asList(1, 2, 3, 4, 5)) -> true
    isSorted(Arrays.asList(1, 3, 2, 4, 5)) -> false
    isSorted(Arrays.asList(1, 2, 3, 4, 5, 6)) -> true
    isSorted(Arrays.asList(1, 2, 3, 4, 5, 6, 7)) -> true
    isSorted(Arrays.asList(1, 3, 2, 4, 5, 6, 7)) -> false
    isSorted(Arrays.asList(1, 2, 2, 3, 3, 4)) -> true
    isSorted(Arrays.asList(1, 2, 2, 2, 3, 4)) -> false
     */
    public boolean isSorted(List<Integer> lst) {
        if (lst == null || lst.size() < 2) return true;
         Map<Long, Long> map = new HashMap<>();
         map.put(0L, Long.valueOf(1));
        for (int i=1; i<lst.size();i++){
            long key = map.get((long) lst.get(i)).longValue() + (long) lst.get(i);
            if (!map.containsKey(key)) {
                map.put((long) lst.get(i), Long.valueOf(1));
            } else return false;
        }
         return true;
    }
}